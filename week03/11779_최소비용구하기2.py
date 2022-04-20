import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

edges = [[] for _ in range(n+1)]
# 다익스트라 알고리즘 적용을 위해 INF로 초기화한 배열 생성
distance = [INF] * (n+1)

for _ in range(m):
    x,y,cost = map(int, input().split())
    edges[x].append([y,cost])

start, end = map(int, input().split())
paths = [[] for i in range(n+1)]


def dijkstar(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    paths[start] = [start]

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in edges[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost,i[0]))
                paths[i[0]] = paths[now] + [i[0]]


dijkstar(start)
print(distance[end])
print(len(paths[end]))
print(*paths[end])