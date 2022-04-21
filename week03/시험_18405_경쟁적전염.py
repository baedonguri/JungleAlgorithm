from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())
que = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            que.append([arr[i][j], i,j, 0])

que.sort()
que = deque(que)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while que:
        val,x,y,time = que.popleft()

        if time == S:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = val
                que.append([val,nx, ny, time+1])
            

bfs()
print(arr[X-1][Y-1])