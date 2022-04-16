import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

check = [[0]*m for i in range(n)]

# delta search를 위한 좌표 배열
dx = [-1,0,1,0]
dy = [0,-1,0,1]

que = deque([(0,0)])
# 1,1 부터 시작하므로 방문표시
check[0][0] = 1

while que:
    x,y = que.popleft()

    # 끝에 도달하면 해당 값을 출력
    if x == n-1 and y == m-1:
        print(check[x][y])

    # delta search로 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동할 x,y좌표가 정상 범위 내에 있으면서
        if 0 <= nx < n and 0 <= ny < m:
            # 이동할 위치에 아직 방문하지 않았고, 이동할 수 있다면(1이라면)
            if check[nx][ny]==0 and maze[nx][ny]==1:
                # 다음 위치에 현재 위치 + 1 값을 저장해줌
                check[nx][ny] = check[x][y] + 1
                # 다음 위치를 탐색하기 위해 큐에 넣어줌
                que.append((nx,ny))

