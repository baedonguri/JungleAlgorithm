# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# # 상, 하, 좌, 우
# delta_row_col = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# # 좌상, 우상, 우하, 좌하
# delta_diagonal = [[-1, -1], [-1, 1], [1, 1], [1, -1]]


dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]


def dfs(x,y):
    arr[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int,input().rstrip().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)


