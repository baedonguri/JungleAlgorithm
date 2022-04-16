import queue
import sys
from collections import deque

input = sys.stdin.readline

N,M,K,X = map(int, input().split())

edges = [[] for _ in range(N+1)]
check = [-1]*(N+1)


for i in range(M):
    x,y = map(int, input().split())
    edges[x].append(y)

queue = deque([X])

# result = []
check[X] = 0

while queue:
    v = queue.popleft()
        
    for u in edges[v]:
        if check[u] == -1:
            check[u] = check[v] + 1
            queue.append(u)
    print(check)
if K not in check:
    print(-1)
else:
    for i in range(1,N+1):
        if check[i] == K:
            print(i)


# print(result)