import sys
input = sys.stdin.readline
string = input().strip()
stack = []
cnt = 0
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        
    else:
        if string[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            cnt += 1
            stack.pop()
print(cnt)