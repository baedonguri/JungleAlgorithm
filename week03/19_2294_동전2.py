from collections import deque
import sys
from tabnanny import check
input = sys.stdin.readline

n, k = map(int, input().split())

coins = set(int(input()) for _ in range(n))

checked = [0] * (k+1)

que = deque()
for coin in coins:
    if coin > k:
        continue
    checked[coin] = 1
    que.append([coin,1])


def bfs():
    while que:
        val, cnt = que.popleft()
        if val == k:
            return cnt

        for coin in coins:
            if val + coin > k:
                continue

            if not checked[val+coin]:
                checked[val+coin] = 1
                que.append([val+coin, cnt+1])
    return 0

result = bfs()
print(result if result else -1)