import heapq
import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(arr, (-n, n))
    else:
        if len(arr) >= 1:
            print(heapq.heappop(arr)[1])
        else:
            print(0)