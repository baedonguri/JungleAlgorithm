import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
cnt = 0
flag = True

for i in range(n):
    num = int(input())
    
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    
    top = stack[-1]
    
    if top == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
        
if flag:
    for i in result:
        print(i)
else:
    print('No')