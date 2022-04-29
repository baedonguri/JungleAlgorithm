import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

def dfs(x,y):
    if x == n-1 and y == n-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        x1, y1 = x + board[x][y], y
        x2, y2 = x, y+board[x][y]
        if 0 <= x1 < n and y1 < n:
            dp[x][y] += dfs(x1,y1)
        if 0 <= x2 < n and y2 < n:
            dp[x][y] += dfs(x2,y2)
    return dp[x][y]

print(dfs(0,0))
            

