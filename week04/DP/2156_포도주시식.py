import sys
input = sys.stdin.readline

n = int(input())
drink  = [0]+[int(input()) for _ in range(n)] + [0]

dp = [0] * (n+2)
dp[1] = drink[1]
dp[2] = drink[1] + drink[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i], dp[i-1])

print(dp[n])