import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
answer = [0]*(n+1)
degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = [0] + list(map(int, input().rstrip()))
    for j in range(1,n+1):
        if tmp[j] == 1:
            graph[j].append(i)
            degree[i] += 1


def topology_sort():
    que = []
    for i in range(1, n+1):
        if degree[i] == 0:
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

print(*answer[1:] if answer.count(0)<=1 else -1)