import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 1000001 

time = 0

while start <= end:
    mid = (start+end)//2
    
    total = 0
    for i in arr:
        total += mid//i
        
    if total >= m:
        time = mid
        end = mid -1
    else:
        start = mid + 1
print(time)