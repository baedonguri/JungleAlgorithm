# pypy3
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def chainedMatrix():
    for l in range(1,n): # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
        for i in range(0,n-l): # 대각선의 우측 한 칸씩 이동
            j = i+l # 현재 대각선에서 몇번째 원소인지
            # 차이가 1밖에 나지 않는 칸
            # 행렬 2개를 그냥 곱해주는 것과 같음
            if l == 1:
                dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
                continue
            dp[i][j] = float('inf')
            # 각 부분행렬의 곱셈횟수 + 두 행렬의 곱셈 횟수
            for k in range(i,j): # k값으로 최적분할 찾기
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])

    print(dp[0][n-1])

chainedMatrix()