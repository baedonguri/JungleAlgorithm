from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
arr = [i for i in range(1,N+1)]

queue = deque(arr)

print('<',end='')
while queue:
    for i in range(K-1):
        queue.append(queue[0])
        queue.popleft()
    print(f'{queue.popleft()}',end='')
    
    if queue:
        print(',',end=' ')

print('>')