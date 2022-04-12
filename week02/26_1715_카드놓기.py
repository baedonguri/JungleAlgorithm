import heapq
import sys
input = sys.stdin.readline

arr = []
cnt = 0
n = int(input())

for i in range(n):
    num = int(input())
    heapq.heappush(arr, num)
    
while True:
    tmp = 0
    if len(arr) <= 1:
        break
        
    for i in range(2):
        tmp += heapq.heappop(arr)
    cnt += tmp
    heapq.heappush(arr, tmp)
    
print(cnt)