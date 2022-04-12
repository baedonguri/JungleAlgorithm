import sys
import heapq
import sys
input = sys.stdin.readline

n = int(input())
locations = [list(map(int, input().split())) for _ in range(n)]
l = int(input())

answer = 0
heap = []
roads = []
for road in locations:
    x, y = road
    if abs(x-y) <= l:
        roads.append(sorted(road))
roads.sort(key= lambda x:x[1])


for road in roads:
    while heap and heap[0][0] < road[1]-l:
        heapq.heappop(heap)
        if not heap:
            break
    heapq.heappush(heap, road)
        
    answer = max(answer, len(heap))

print(answer)