from sys import stdin
from collections import deque
input = stdin.readline

a,b = map(int, input().split())
que = deque([(a,1)])

while que:
    n, cnt = que.popleft()
    if n > b:
        continue
    if n == b:
        print(cnt)
        break

    que.append((int(str(n)+'1'), cnt+1))
    que.append((n*2, cnt+1))

else:
    print(-1)


