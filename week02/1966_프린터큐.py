import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    
    check = [0] * N
    check[M] = 1
    
    queue = deque(queue)
    check = deque(check)
    
    cnt = 0
    
    while True:
        if queue[0] == max(queue):
            cnt += 1
            
            if check[0] != 1:
                queue.popleft()
                check.popleft()
            else:
                print(cnt)
                break
        else:
            queue.append(queue.popleft())
            check.append(check.popleft())