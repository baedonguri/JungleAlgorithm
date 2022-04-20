from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

# 노드와 간선의 정보 저장
building = [[] for _ in range(n+1)]
# 진입차수
indegree = [0] * (n+1)
# 건물을 짓는데 걸리는 시간
cost = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().rstrip().split()))[:-1]
    cost[i] = data[0]
    building_data  = data[1:]

    # 간선 연결 및 진입차수 설정
    for j in building_data:
        building[j].append(i)
        indegree[i] += 1


def topology_sort():
    result = [0] * (n+1)
    que = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물을 짓는데 걸리는 시간이 포함되어 있음
        # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장
        result[now] += cost[now]
        for b in building[now]:
            indegree[b] -= 1
            result[b] = max(result[b], result[now])
            if indegree[b] == 0:
                que.append(b)
    return result

answer = topology_sort()
for i in range(1, n+1):
    print(answer[i])