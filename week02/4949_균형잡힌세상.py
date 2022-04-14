import sys
input = sys.stdin.readline

def check(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])

        if string[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
                
        if string[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if stack and string[i] == ".":
            return False
    return True
result = []
while True:
    string = input().rstrip()
    if string == ".":
        break
    
    if check(string):
        result.append('yes')
    else:
        result.append('no')        

for i in result:
    print(i)