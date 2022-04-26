import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(3):
        r,g,b = rgb[i-1]
        if j == 0: tmp = min(g,b)
        elif j == 1: tmp = min(r,b)
        else: tmp = min(r,g)
        rgb[i][j] += tmp
    
print(min(rgb[-1]))
