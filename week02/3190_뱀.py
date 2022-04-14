# -*- coding: utf-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*N for _ in range(N)]
direction = {0 : (0,1), 1 : (1,0), 2: (0,-1), 3 : (-1,0)}
q = deque() # 뱀 몸통
commend = deque() # 명령을 저장해둘 큐

K = int(input())
for i in range(K):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1
    
L = int(input())
for i in range(L):
    X, C = input().split()
    commend.append([int(X),C])


d = 0
cnt = 0
nx, ny = 0,0
q.append((nx,ny))
arr[nx][ny] = 2


while True:
    cnt += 1
    nx = nx + direction[d][0]
    ny = ny + direction[d][1]
    
    if not 0 <= nx < N or not 0 <= ny < N: #뱀이 격자 밖으로 나가면 게임이 종료
        break
    if arr[nx][ny] == 1:
        arr[nx][ny] = 2
        q.append((nx,ny))
    elif arr[nx][ny] == 0:
        arr[nx][ny] = 2
        q.append((nx,ny))
        delX, delY = q.popleft()
        arr[delX][delY] = 0
    elif arr[nx][ny] == 2: # 자기 몸에 닿을 경우 게임 종료
        break
    
    if len(commend) and commend[0][0] == cnt:
        t, nd = commend.popleft()
        if nd == 'L':
            d = (d+3)%4
        elif nd == 'D':
            d = (d+1)%4
print(cnt)