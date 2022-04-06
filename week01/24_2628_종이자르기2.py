from bisect import insort
from sys import stdin
input = stdin.readline

w, h = map(int, input().split())
n = int(input())

x_pos, y_pos = [0,h], [0,w]

for i in range(n):
    direction, idx = map(int, input().split())
    if direction == 0:
        insort(x_pos, idx)
    else:
        insort(y_pos, idx)

max_area = 0
for i in range(len(x_pos)-1):
    for j in range(len(y_pos)-1):
        area = (x_pos[i+1]-x_pos[i])*(y_pos[j+1]-y_pos[j])
        if area > max_area:
            max_area = area
            
print(max_area)