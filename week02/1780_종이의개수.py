import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

cnt = [0,0,0]
def solve(x,y,n):
    num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                solve(x, y, n // 3) #1
                solve(x, y+n//3, n // 3) #2
                solve(x, y+n//3*2, n // 3) #3

                solve(x+n//3, y, n // 3) #4
                solve(x+n//3, y+n//3, n // 3) #5
                solve(x+n//3, y+n//3*2, n // 3) #6
                
                solve(x+n//3*2, y, n // 3) #7
                solve(x+n//3*2, y+n//3, n // 3) #8
                solve(x+n//3*2, y+n//3*2, n // 3) #9
                return
    if num == -1:
        cnt[0] +=1
    elif num == 0:
        cnt[1] += 1
    elif num == 1:
        cnt[2] += 1


solve(0,0, n)

for i in cnt:
    print(i)