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

# 시작 도시로부터 다른 도시까지의 최소 비용 갱신
def dijkstar(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        # 최단 거리인 노드에 대한 정보를 꺼냄
        dist, now = heapq.heappop(que)
        # 이미 처리된 노드라면 pass
        if distance[now] < dist:
            continue
        # 선택된 노드와 인접한 노드를 확인
        for i in edges[now]:
            # 비용 합산
            cost = dist + i[1]
            # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우 갱신해주기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost,i[0]))

# 시작위치에서 다른 도시까지의 거리 산출
dijkstar(start)
# 도착위치의 최소 비용을 확인
print(distance[end])
