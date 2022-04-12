import sys
input = sys.stdin.readline

l_stack = list(input())
r_stack = []
num = int(input())
for i in range(num):
    commend = list(map(str, input().split()))
    
    if commend[0] == 'L':
        if l_stack:
            r_stack.append(l_stack.pop())
        else: continue

    elif commend[0] == 'D':
        if r_stack:
            l_stack.append(r_stack.pop())
        else: continue
        
    elif commend[0] == 'B':
        if l_stack:
            l_stack.pop()
        else: continue
    elif commend[0] == 'P':
        l_stack.append(commend[1])
    
        
print(''.join(l_stack+list(reversed(r_stack))))