import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parts = [[0]*(n+1) for _ in range(n+1)]

que = deque()

degree = [0] * (n+1)

for _ in range(int(input())):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))
    degree[a] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        que.append(i)


while que:
    now = que.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지 검사
    for next, next_need in graph[now]:
        # 현재 제품이 일반 부품이라면
        if parts[now].count(0) == n+1:
            # 가중치만큼 더 해줌
            parts[next][now] += next_need

        # 현재 제품이 중간 부품이라면
        else:
            for i in range(1, n+1):
                # 현재 가진 부품 * 가중치를 다음 위치에 저장해줌
                parts[next][i] += parts[now][i] * next_need
    # 연결 해제
        degree[next] -= 1
        # 진입차수가 0이라면 큐에 삽입
        if degree[next] == 0:
            que.append(next)

# 해당 부품에 대한 정보 출력
for idx, x in enumerate(parts[n]):
    if x > 0:
        print(idx, x) 
