from math import inf
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = inf

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1, v2 = map(int,input().split())


def dijkstra(start,end):
    dist = [INF] * (v+1)
    dist[start] = 0
    heap = []
    heappush(heap, [0, start])

    while heap:
        now_cost, node = heappop(heap)
        if now_cost > dist[node]:
            continue
        for next_cost, next_node in graph[node]:
            next_cost += now_cost

            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heappush(heap, [next_cost, next_node])

    return dist[end]


result1 = 0
result2 = 0

result1 += dijkstra(1,v1)
result1 += dijkstra(v1,v2)
result1 += dijkstra(v2,v)


result2 += dijkstra(1,v2)
result2 += dijkstra(v2,v1)
result2 += dijkstra(v1,v)


answer= min(result1, result2)

print(-1 if answer == INF else answer)