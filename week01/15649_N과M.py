import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0] * n

temp = []

def func():
    if len(temp) == m:
        print(' '.join(map(str, temp)))
        return
    
    for i in range(n):
        if visited[i]: continue
        visited[i] = 1
        temp.append(i+1)
        func()
        visited[i] = 0
        temp.pop()

func()