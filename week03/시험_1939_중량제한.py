# -*- coding: utf-8 -*-
import sys
from heapq import heappush, heappop
from math import inf
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
chkCost = [inf] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,c = map(int, input().split())
    graph[x].append((y,c))
    graph[y].append((x,c))

v1, v2 = map(int, input().split())
max_weight = 0

# 기본 다익스트라
def dijkstra(start, end):
    heap = []
    heappush(heap, (0,start))
    chkCost[start] = 0
    
    while heap:
        now_cost, node = heappop(heap)
        
        for next_node, next_cost in graph[node]:
            next_cost += -(now_cost)
            if chkCost[next_node] > next_cost:
                chkCost[next_node] = next_cost
                heappush(heap, [-next_cost,next_node])
    return chkCost[end]

max_weight = dijkstra(v1,v2)

print(max_weight)
#최대 다익스트라?
#구현 x
