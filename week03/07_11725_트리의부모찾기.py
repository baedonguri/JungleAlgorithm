from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
check = [False]*(n+1)
answer = [0]*(n+1)
for _ in range(n-1):
    x,y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


# def dfs(v):
#     check[v] = True
#     for i in edges[v]:
#         if check[i] == False:
#             answer[i] = v
#             dfs(i)
# dfs(1)

def bfs(n):
    que = deque([n])
    check[n] = True
    while que:
        v = que.popleft()
        for i in edges[v]:
            if not check[i]:
                answer[i] = v
                que.append(i)
                check[i] = True 
        
bfs(1)

for i in answer[2:]:
    print(i)