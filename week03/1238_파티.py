import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))

# 다익스트라 알고리즘
def dijkstra(start):
    distance = [INF] * (n+1)

    heap = []
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        now_cost, node = heappop(heap)
        for next_cost, next_node in graph[node]:
            next_cost += now_cost
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heappush(heap, (next_cost, next_node))
    

    return distance
answer = [0] * (n+1)
for i in range(1, n+1):
    # 시작노드 바꿔가며 다른 도시로 가는 최소비용 계산
    arr = dijkstra(i)
    # 파티가 열리는 장소까지의 거리를 answer에 저장
    answer[i] += arr[x]
    # 파티 장소에서 다른 도시로 가는 최소 비용 계산
    arr2 = dijkstra(x)
    # 파티장소에서 각 도시로 돌아가는 비용을 더해줌 => 왕복 비용 산출 완료
    answer[i] += arr2[i]
# 가장 오래 걸리는 녀석을 산출
print(max(answer))