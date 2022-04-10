import sys
input = sys.stdin.readline

string = input().strip()
stack = []
answer = 0
tmp = 1

for i in range(len(string)):
    if string[i] == '(':
        tmp *= 2
        stack.append(string[i])
    elif string[i] == '[':
        tmp *= 3
        stack.append(string[i])
        
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if string[i-1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
    else: # string[i] == ']'
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if string[i-1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()
    
if stack:
    answer = 0
    
print(answer)