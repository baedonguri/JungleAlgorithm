from collections import deque, Counter
from functools import reduce
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(n)]

checked = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y,cnt):
    que = deque([])
    que.append([x,y])
    checked[x][y] = cnt
    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if arr[nx][ny] == 1 and checked[nx][ny] == 0:
                que.append([nx,ny])
                checked[nx][ny] = cnt

cnt = 0
nums = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and checked[i][j] == 0:
            cnt += 1
            bfs(i,j, cnt)

print(cnt)

answer = reduce(lambda x,y : x+y, checked)

answer=  [x for x in answer if x>0]

answer = sorted(list(Counter(answer).values()))

print('\n'.join(map(str,answer)))


