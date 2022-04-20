from collections import deque
import sys
input = sys.stdin.readline
limit = int(1e5)

n, k = map(int, input().rstrip().split())
dist = [-1] * (limit+1)
cnt = 0
def bfs():
    global cnt
    que = deque([n])
    dist[n] = 0
    while que:
        x = que.popleft()
        if x == k:
            cnt += 1
        for next in (x*2, x+1, x-1):
            if 0 <= next <= limit:
                if dist[next] == -1 or dist[next]>= dist[x]+1:
                    dist[next] = dist[x] + 1
                    que.append(next) 
            

bfs()
print(dist[k])
print(cnt)