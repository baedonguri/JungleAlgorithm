import sys
input = sys.stdin.readline

n,k = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(n)]

coins.sort(reverse=True)

cnt = 0
tmp = 0
for coin in coins:
    if k < coin:
        continue
    
    coin 