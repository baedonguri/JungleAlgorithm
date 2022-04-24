import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*91

dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
print(dp)


# def fibo(x):
#     if x==1 or x ==2:
#         return 1
#     if dp[x] != 0:
#         return dp[x]

#     dp[x] = fibo(x-1) + fibo(x-2)
#     return dp[x]

print(fibo(n))
    
