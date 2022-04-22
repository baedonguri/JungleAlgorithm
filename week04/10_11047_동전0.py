import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))

result = 0

for i in range(N-1,-1,-1):
    result += (K//coins[i])
    K %= coins[i]
print(result)