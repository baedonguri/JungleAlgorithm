from collections import deque

def check_last(n):
    return 1 if len(n) == 1 else 0

def solution(n, edge):
    answer = 0
    check = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)

    que = deque([1])
    check[1] = 1
    while que:
        q = que.popleft()
        for v in graph[q]:
            if not check[v]:
                check[v] = check[q]+1
                que.append(v)  
    
    max_v = max(check)
    return check.count(max_v)

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n,edge))

