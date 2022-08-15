from sys import stdin
from collections import deque

input = stdin.readline
n,m = map(int, input().rstrip().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    que = deque([start])

    while que:
        q = que.popleft()
        for i in graph[q]:
            if i not in visited:
                num[i] = num[q] + 1
                visited.append(i)
                que.append(i)
    return sum(num)


for i in range(1, n+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)