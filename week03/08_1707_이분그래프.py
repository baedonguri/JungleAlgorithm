import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n, u):
    check[n] = u # 해당 정점에 group을 설정(-1,1)
    for i in edges[n]:
        if not check[i]: # 만약 방문하지 않았다면
            a = dfs(i, -u)  # 그룹값을 -1로 주고 dfs 수행
            if not a: #  하나라도 False라면 이분그래프가 아니므로 바로 False 때리기
                return False
        elif check[i] == check[n]: # 만약 현재 정점과 연결된 정점의 그룹값이 같다면 False 리턴
            return False
    return True # 나머지 경우는 True 리턴

k = int(input())

for _ in range(k):
    v,e = map(int, input().split())

    edges = [[] for _ in range(v+1)]
    check = [False]*(v+1)

    for _ in range(e):
        x,y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)

    for i in range(1,v+1):
        if not check[i]: # 방문한 정점이 아니면 dfs 수행
            result = dfs(i,1) #초기는 그룹값을 1로 주고 수행
            if not result: # result가 False가 나왔다면 더 이상 수행할 필요가 없음
                break

    print('YES' if result else 'NO')