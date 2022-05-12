from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,v = map(int, input().split())

check = [False] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    check[v] = True
    print(v, end=' ')
    for u in graph[v]:
        if not check[u]:
            dfs(u)
def bfs(v):
    check[v] = True
    que = deque([v])
    while que:
        u = que.popleft()
        print(u, end=' ')
        for i in graph[u]:
            if not check[i]:
                check[i] = True
                que.append(i)
dfs(v)

check = [False] * (n+1)
print()

bfs(v)