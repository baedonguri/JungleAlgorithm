# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)

ans = 0

while start <= end:
    mid = (start+end)//2
    cnt = 1
    total = 0
    for i in range(N):
        if total + arr[i] <= mid:
            total += arr[i]
        
        else:
            cnt += 1
            total = arr[i]
        
        if cnt > M:
            break
    
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
        
print(ans)
        