from collections import deque
def solution(maps):
    answer = 0
    que = deque()
    que.append([0,0])
    maps[0][0] = 1
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    while que:
        q = que.popleft()
        x,y = q
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps[0])-1 and 0 <= ny < len(maps)-1:
                if maps[nx][ny]:
                    maps[nx][ny] = maps[nx][ny] + 1
                    que.append([nx,ny])
                    
            if nx == len(maps[0])-1 and ny == len(maps)-1:
                return maps[-1][-1]
                    
    return -1