import sys
input = sys.stdin.readline

N = int(input())
row_info, plus_info, minus_info = [1]*N, [1]*(2*N-1),[1]*(2*N-1)
cnt = [0]

def queen(col=0):
    if col == N:
        cnt[0] += 1
        return
    
    for row in range(N):
        if row_info[row] and plus_info[row+col] and minus_info[row-col]:
            row_info[row],plus_info[row+col],minus_info[row-col] = 0,0,0
            queen(col+1)
            row_info[row],plus_info[row+col],minus_info[row-col] = 1,1,1

queen(0)

print(cnt[0])