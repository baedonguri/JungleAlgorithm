import sys
input = sys.stdin.readline

def VPS(string):
    stack = []
    
    for s in string:
        if s == '(':
            stack.append(s)
        
        if s == ')' and len(stack) == 0:
            return False
        elif s == ')':
            stack.pop()
    
    return True if len(stack) == 0 else False

for i in range(int(input())):
    string = input()
    
    if VPS(string):
        print('YES')
    else:
        print('NO')