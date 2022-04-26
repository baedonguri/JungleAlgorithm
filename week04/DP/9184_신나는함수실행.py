import sys
input = sys.stdin.readline


for _ in range(int(input())):
    dp = [0,1,1,1,2]
    n = int(input())

    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-5])
        
    print(dp[n])