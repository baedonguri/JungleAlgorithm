import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
A = [list(map(int,input().strip().split())) for _ in range(N)]
M,K = map(int, input().strip().split())
B = [list(map(int,input().strip().split())) for _ in range(M)]

arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(M):
            arr[i][j] += A[i][k]*B[k][j]

for i in arr:
    print(i)