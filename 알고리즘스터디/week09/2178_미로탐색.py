from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    que = deque([(0,0)])
    check[0][0] = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0 <= ny < n and 0 <= nx < m and not check[ny][nx] and maze[ny][nx]:
                check[ny][nx] = check[y][x] + 1
                que.append([ny,nx])

    return check[-1][-1]

print(bfs())

'''
안녕하세요 배동준님
'''