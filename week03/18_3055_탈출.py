from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())

forest = [list(map(str, input().rstrip())) for _ in range(r)]

check = [[0]*c for i in range(r)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

que = deque([])
cave = []

for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            que.append([i,j])
        elif forest[i][j] == 'S':
            que.appendleft([i,j])
        elif forest[i][j] == 'D':
            cave = [i,j]

flag = False
while que:
    if flag: break

    x,y = que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < r and 0 <= ny < c):
            continue
            
        if forest[x][y] == '*':
            if forest[nx][ny] == '.' or forest[nx][ny] == 'S':
                forest[nx][ny] = '*'
                que.append([nx,ny])

        elif forest[x][y] == 'S':
            if forest[nx][ny] == '.':
                forest[nx][ny] = 'S'
                check[nx][ny] = check[x][y] + 1
                que.append([nx,ny])

            elif forest[nx][ny] == 'D':
                check[nx][ny] = check[x][y] + 1
                flag = True
                break
            

print('KAKTUS' if not check[cave[0]][cave[1]] else check[cave[0]][cave[1]])