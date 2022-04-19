import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
answer = [0] * (n+1) # 최종 결과를 저장할 공간
degree = [0] * (n+1) # 진입 차수를 저장할 공간
graph = [[] for _ in range(n+1)] # 인접리스트

# 인접리스트 생성
for i in range(1, n+1):
    tmp = [0] + list(map(int, input().rstrip()))
    for j in range(1, n+1):
        if tmp[j]:
            graph[j].append(i)
            degree[i] += 1

def topology_sort():
    que = []
    # 진입 차수가 0인 노드부터 삽입 
    # 진입방향을 바꾸기 위해 최대힙을 통해 최대값을 먼저 출력하여
    # 맨 뒤로 밀어주는 방법
    for i in range(1, n+1):
        if not degree[i]:
            heappush(que, -i)
        
    N = n
    while que:
        now = -heappop(que)
        answer[now] = N

        for i in graph[now]:
            degree[i] -= 1

            if degree[i] == 0:
                heappush(que, -i)

        N -= 1

topology_sort()

if answer.count(0) > 1: print(-1)
else: print(*answer[1:])