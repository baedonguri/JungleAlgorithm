import heapq
import sys
input =sys.stdin.readline

n, k = map(int, input().split())
jewelrys = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

max_value = 0
tmp = []

jewelrys.sort(key=lambda x:x[0])
bags.sort()

for bag_weight in bags:
    while jewelrys and bag_weight >= jewelrys[0][0]:
        heapq.heappush(tmp, -(jewelrys[0][1]))
        heapq.heappop(jewelrys)
        
    if tmp:
        max_value += heapq.heappop(tmp)
    elif not jewelrys:
        break

print(-max_value)