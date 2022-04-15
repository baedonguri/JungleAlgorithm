import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    check[v] = True
    for i in edge[v]:
        if not check[i]:
            dfs(i)

n,m = map(int, input().split())

edge = [[] for i in range(n+1)]
check = [False]*(n+1)
cnt = 0

for i in range(m):
    x,y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)


for j in range(1, n+1):
    if not check[j]:
        dfs(j)
        cnt += 1

print(cnt)
