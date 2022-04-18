import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1


que = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

def topology_sort():
    result = []
    while que:
        now = que.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                que.append(i)

    print(' '.join(map(str, result)))


topology_sort()