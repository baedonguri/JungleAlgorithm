import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

cur_max = lst.pop()
cnt = 1

for i in lst[::-1]:
    if i > cur_max:
        cnt += 1
        cur_max = i

print(cnt)