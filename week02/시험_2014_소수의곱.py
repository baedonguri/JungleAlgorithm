import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().strip().split())
prime = list(map(int, input().strip().split()))

heap = []

for i in prime:
    heapq.heappush(heap, i)
    
    
for i in range(k):
    temp = heapq.heappop(heap)
    for j in range(n):
        new_num = temp*prime[j]
        heapq.heappush(heap, new_num)
        
        if temp%prime[j] == 0:
            break
            
print(temp)