from collections import deque
import sys
input = sys.stdin.readline
limit = int(1e5)

n, k = map(int, input().rstrip().split())
dist = [0] * (limit+1)


def bfs():
    que = deque([n])
    while que:
        x = que.popleft()
        if x == k:
            print(dist[x])
            break
        
        for next in (x-1,x+1,x*2):
            if 0 <= next <= limit and not dist[next]:
                dist[next] = dist[x] + 1
                que.append(next)  
bfs()
