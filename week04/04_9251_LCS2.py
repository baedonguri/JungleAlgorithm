import sys
input = sys.stdin.readline

def lcs(X,Y):
    m = len(X)
    n = len(Y)
    # dp 값을 저장하기 위한 배열
    L = [[None]*(n+1) for _ in range(m+1)]

    # L[m+1][n+1]을 bottom up 방식으로 채워나감
    # L[i][j]는 LCS의 길이를 가지고 있음
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: # 각 문자열의 끝이 같다면
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m-1][n-1] # 해당 위치에 LCS의 최종 길이가 저장

x = input()
y = input()

print(lcs(x,y))