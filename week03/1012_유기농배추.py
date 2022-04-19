import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,k = map(int, input().split())

    arr = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]

    for _ in range(k):
        y,x = map(int, input().split())
        arr[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def dfs(x,y):
        check[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<= nx < m and 0 <= ny < n):
                continue
            if arr[ny][nx] and not check[ny][nx]:
                arr[ny][nx] = -1
                dfs(nx,ny)
            
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[j][i] and not check[j][i]:
                dfs(i,j)
                cnt += 1

    print(cnt)