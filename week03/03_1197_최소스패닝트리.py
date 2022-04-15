import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
edge = [[] for i in range(V+1)]
check = [False]*(V+1)
result = 0

for i in range(E):
    a,b,c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if check[each_node] == False:
        check[each_node] = True
        result += w
        for next_edge in edge[each_node]:
            if check[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(result)