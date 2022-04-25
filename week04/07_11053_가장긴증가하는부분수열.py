import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n


for i in range(n):
    # 자신을 포함하여 만들 수 있는 부분 수열의 크기를 저장
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
