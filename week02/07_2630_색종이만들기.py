# -*- coding: utf
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for n in range(n)]

cnt = [0, 0] # index 0 : white-card, index 1 : blue-card

def solve(N, paper):
    total = 0 # 색종이의 합을 구하기 위한 임시 변수
    
    # 입력된 배열(색종이)의 전체 합을 구함
    for i in range(N):
        total += sum(paper[i])

    if total == 0:     # 색종이의 전체합이 0이라면 white-card 카운트
        cnt[0] += 1
    elif total == N*N: # 색종이의 전체합이 1이라면 blue-card 카운트
        cnt[1] += 1
    else: # 위의 경우가 아니라면 색종이의 크기가 1이 될 때까지 4등분 분할 후 재귀
        temp = [paper[i][0:N//2] for i in range(0,N//2)] # 1사분면
        solve(N//2, temp) 
        temp = [paper[i][N//2:] for i in range(0,N//2)] # 2사분면
        solve(N//2, temp)
        temp = [paper[i][0:N//2] for i in range(N//2,N)] # 3사분면
        solve(N//2, temp)
        temp = [paper[i][N//2:N] for i in range(N//2,N)] # 4사분면
        solve(N//2, temp)


solve(n, arr)
print(cnt[0]) # white-card
print(cnt[1]) # blue-card