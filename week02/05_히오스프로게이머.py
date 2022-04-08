import sys
input = sys.stdin.readline

N, K = map(int, input().split())
levels = [int(input()) for _ in range(N)]
levels.sort()

start,end = min(levels), max(levels) + K
result = 0

while start <= end:
    mid = (start+end)//2
    total = 0
    
    total = sum([mid-i for i in levels if mid > i])
    
    if total <= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)