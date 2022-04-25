import sys
input = sys.stdin.readline
INF = float("inf")
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF]*(1<<n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1<<n) - 1: # 모든 도시를 방문했을 때
        if graph[x][0]: # 출발점으로 가는 경로가 있을 경우
            return graph[x][0] # 출발점으로 가는 비용을 반환
        else:
            return INF # 출발점으로 가는 경우가 없다면 유효하지 않은 경로

    if dp[x][visited] != INF: # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]
    
    for i in range(1,n): # 모든 도시를 탐방
        if not graph[x][i]: # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i): # 이미 방문한 도시라면 skip
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1<<i)) + graph[x][i])
    
    return dp[x][visited]

print(dfs(0,1))
# for i in dp:
#     print(i)