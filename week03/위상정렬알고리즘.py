from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# 진입차수
indegree = [0] * (v+1)
# 인접 리스트
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    que = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                que.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()