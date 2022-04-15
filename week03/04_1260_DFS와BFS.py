"""
1. 아이디어 
- DFS
- 시작 위치를 정해준다.
- 시작 위치를 방문하고, 방문 표시를 해준다.
    - 인접 리스트를 탐색한다.
        - 만약 아직 방문하지 않은 인접 리스트가 있다면
            - dfs로 방문한다.

- BFS
- 시작 위치를 정해준다.
- 시작 위치를 방문하고, 방문 표시를 해준다.
    - 인접 리스트를 탐색한다.
        - 만약 아직 방문하지 않은 인접 리스트가 있다면
            - 큐에 넣어주고, 해당 vertex를 방문처리한다.
"""



import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
edge = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    x,y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)

for i in range(1, n+1):
    edge[i].sort()


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in edge[n]:
        if not visited[i]:
            dfs(i)

dfs(v)
visited = [False]*(n+1)
print()



def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in edge[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(v)