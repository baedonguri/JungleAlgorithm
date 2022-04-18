import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
check = [[False]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
result = []

def dfs(x,y):
    global cnt
    cnt += 1
    check[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if arr[nx][ny] and not check[nx][ny]:
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if arr[i][j] and not check[i][j]:
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()

print('\n'.join(map(str, result)))