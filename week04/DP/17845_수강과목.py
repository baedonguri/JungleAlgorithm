import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(k+1)]
grades = []
times = []

for _ in range(k):
    g,t = map(int, input().split())
    grades.append(g)
    times.append(t)


for i in range(1,k+1):
    for j in range(1, n+1):
        if times[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(grades[i-1]+dp[i-1][j-times[i-1]], dp[i-1][j])

print(dp[k][n])