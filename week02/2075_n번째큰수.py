import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    rows = list(map(int, input().split()))
    
    if not heap:
        for row in rows:
            heapq.heappush(heap, row)
    else:
        for row in rows:
            if heap[0] < row:
                heapq.heappush(heap, row)
                heapq.heappop(heap)
print(heap[0])