import sys

input = sys.stdin.readline

w,h = map(int, input().split())
n = int(input())

x_ = [0]
y_ = [0]

for i in range(n):
    direction, idx = map(int, input().split())
    if direction == 0:
        x_.append(idx)
    else:
        y_.append(idx)
    

x_.append(h)
y_.append(w)

x_.sort()
y_.sort()


t_arr = []
for i in range(len(x_)-1):
    for j in range(len(y_)-1):
        result = (x_[i+1]-x_[i]) * (y_[j+1]-y_[j])
        t_arr.append(result)

print(max(t_arr))