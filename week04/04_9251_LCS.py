import sys
input = sys.stdin.readline

string1 = list(input().rstrip())
string2 = list(input().rstrip())

len1 = len(string1)
len2 = len(string2)

dp = [[0]*(len2+1) for _ in range(len1+1)]

for i in range(1, len1 + 1):
    for j in range(1, len2+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
        