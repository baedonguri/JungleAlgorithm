from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
family = [[] for _ in range(n+1)]
check = [False]*(n+1)
p1, p2 = map(int, input().split())

m = int(input())

for _ in range(m):
    x,y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

def bfs(v1,v2):
    cnt = 0
    que = deque([[v1,cnt]])
    
    while que:
        v, count = que.popleft()
        if v == v2:
            return count
        
        if not check[v]:
            count += 1
            check[v] = True
            for e in family[v]:
                if not check[e]:
                    que.append([e, count])

    return -1

# def bfs(v1,v2):
#     cnt = 0
#     que = deque([[v1, cnt]])
#     check[v1] = True
#     while que:
#         val, count = que.popleft()

#         if val == v2:
#             return count 
#         for u in family[val]:
#             if not check[u]:
#                 que.append([u, count+1])
#                 check[u] = True
#     return -1

print(bfs(p1,p2))