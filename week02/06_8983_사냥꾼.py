import sys
input = sys.stdin.readline

M,N,L = map(int, input().split())
lines = list(map(int, input().split()))
targets = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
start, end = 0, M-1
cnt = 0

for i in range(len(targets)):
    start, end = 0, M-1
    while start <= end:
        mid = (start+end)//2
        if abs(lines[mid] - targets[i][0])+targets[i][1] <= L:
            cnt += 1
            break
        if targets[i][0] > lines[mid]:
            start = mid + 1
        else:
            end = mid - 1
print(cnt)