from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())
network = [[] for i in range(n+1)]
check = [False] * (n+1)

answer = []
for i in range(k):
    x,y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)
    
def dfs(v):
    check[v] = True
    for q in network[v]:
        if not check[q]:
            answer.append(q)
            dfs(q)

dfs(1)
print(len(answer))