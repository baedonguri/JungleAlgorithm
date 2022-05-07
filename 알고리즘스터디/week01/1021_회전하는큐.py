from collections import deque
from sys import stdin

input = stdin.readline


n, m = map(int, input().split())
que = deque([i for i in range(1,n+1)])

arr = list(map(int, input().split()))

cnt = 0 
for num in arr:
    while True:
        if que[0] == num:
            que.popleft()
            break
        else:
            if que.index(num) <= len(que)//2:
                que.rotate(-1)
                cnt += 1
            else:
                que.rotate(1)
                cnt += 1

print(cnt)