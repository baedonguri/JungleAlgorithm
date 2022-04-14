from collections import deque
import sys
input = sys.stdin.readline

num = int(input())

arr = deque([])

for i in range(num):
    commend = input().split()
    
    if commend[0] == 'push_front':
        arr.appendleft(int(commend[1]))

    elif commend[0] == 'push_back':
        arr.append(int(commend[1]))
        
    elif commend[0] == 'pop_front':
        if len(arr) == 0: print(-1)
        else:
            print(arr[0])
            arr.popleft()
            
    elif commend[0] == 'pop_back':
        if len(arr) == 0: print(-1)
        else:
            print(arr[-1])
            arr.pop()
            
    elif commend[0] == 'size':
        print(len(arr))
    
    elif commend[0] == 'empty':
        if len(arr) == 0: print(1)
        else: print(0)
            
    elif commend[0] == 'front':
        if len(arr) == 0: print(-1)
        else: print(arr[0])

    elif commend[0] == 'back':
        if len(arr) == 0: print(-1)
        else: print(arr[-1])