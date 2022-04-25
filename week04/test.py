from sys import stdin
input = stdin.readline
INF = float('inf')
def dfs(x, visited):
    if visited == (1 << N) - 1:
        return graph[x][0] if graph[x][0] else INF
    if dp[x][visited] != INF:
        return dp[x][visited]
    for i in range(1, N):           # 모든 도시를 탐방 (0번 도시 제외)
        if not graph[x][i] or visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]
N = int(input())
dp = [[INF] * (1 << N) for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
print(dfs(0, 1))
for d in dp:
    print(*d)