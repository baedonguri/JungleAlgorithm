from collections import deque
from sys import stdin
input = stdin.readline

def getPrime():
    m = 10000
    arr = [0,0] + [1] * (m-1)
    for i in range(2, int(m**0.5)+1):
        for j in range(i+i, m+1, i):
            if arr[i]: arr[j] = 0
    return arr
primes = getPrime()

def bfs():
    que = deque()
    que.append([x,0])
    visited = [0] * 10000
    visited[x] = 1

    while que:
        num, cnt = que.popleft()
        if num == y: return cnt
        if num < 1000: continue

        for i in [1,10,100,1000]:
            n = num - num % (i*10)//i*i
            for j in range(10):
                if not visited[n] and primes[n]:
                    visited[n] = 1
                    que.append([n, cnt + 1])
                n += i        

for i in range(int(input())):
    x,y = map(int, input().split())
    result = bfs()
    print(result if result else 0)
