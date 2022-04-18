import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

y, x = map(int, input().strip().split(' '))

ice = [list(map(int, input().strip().split(' '))) for _ in range(y)]

stack = [] # 빙하 정보가 있는 리스트에서 1년 후에 얼마를 빼줘야 할지를 저장하기 위한 스택


# 상하좌우
dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0] 

answer = 0
def water(i, j): return 1 if ice[i][j] <= 0 and 0 <= i < y and 0 <= j < x else 0
def dfs(i, j, visited): # 현재 얼음덩이가 몇덩이 인지 확인해주는 것
    noi = 1
    visited.add((i, j))
    # visited[i][j] = 1
    for k in range(4): # i+dy[k], j+dx[k]
        n1 = i+dy[k]
        n2 = j+dx[k]
        if (n1, n2) not in visited and ice[n1][n2] > 0 and 0 <= n1 < y and 0 <= n2 < x:
            noi += dfs(n1, n2, visited)
    return noi
while True:
    answer += 1
    if answer == 1:
        for i in range(y): # 행
            for j in range(x): # 열
                cnt = 0
                if ice[i][j] > 0:
                    for k in range(4):
                        cnt += water(i+dy[k], j+dx[k])
                    stack.append((i, j, cnt))
    else:
        for i in iceGroup:
            cnt = 0
            if ice[i[0]][i[1]] > 0:
                    for k in range(4):
                        cnt += water(i[0]+dy[k], i[1]+dx[k])
                    stack.append((i[0], i[1], cnt))
    total_ice = 0
    iceGroup = []
    unmelt = 0
    while stack: # 0으로 따로 처리하지 말고, 나중에 물은 0이하의 수로 지정
        tmp = stack.pop()
        tmp2 = ice[tmp[0]][tmp[1]] - tmp[2]
        ice[tmp[0]][tmp[1]] = tmp2
        if tmp2 > 0:
            iceGroup.append((tmp[0], tmp[1]))
            total_ice += 1
            unmelt = (tmp[0], tmp[1])
    if unmelt == 0:
        answer = 0
        break
    rev_ice = 0
    visited = set()
    rev_ice += dfs(unmelt[0], unmelt[1], visited)
    if total_ice != rev_ice:
        break
print(answer)