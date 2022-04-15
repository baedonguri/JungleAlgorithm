import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
k = int(input())

cnt = [-1]
edges = [[] for i in range(n+1)]
check = [False] * (n+1)

for i in range(k):
    x,y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


def dfs(v):
    check[v] = True
    cnt[0] += 1
    for i in edges[v]:
        if check[i] == False:
            dfs(i)


if not check[1]:
    dfs(1)

print(*cnt)