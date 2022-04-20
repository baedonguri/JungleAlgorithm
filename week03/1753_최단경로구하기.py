import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int, input().split())
start = int(input())
distance = [0]+[INF]*v

graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])


def dijkstra(start):
    que = []
    heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heappop(que)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(que, (cost, i[0]))

dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)