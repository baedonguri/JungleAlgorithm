# p = "(()())()"
p = "()))((()"

def solution(p):
    answer, u, v = '', '', ''
    
    if p == '' or correct(p): return p
    
    for i in range(2,len(p)+1,2):
        if balanced(p[0:i]):
            u =p[0:i]
            v=p[i:]
            break
    
    if u[0] == '(':
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        if len(u) > 2:
            tmp += ''.join(['(' if x==')' else ')' for x in u[1:len(u)-1]])
        return tmp


def balanced(string):
    if string.count('(') == string.count(')'):
        return True
    return False

def correct(string):
    stack = []
    stack.append(string[0])
    for i in range(1, len(string)):
        if not stack or stack[-1] == ')' or (stack[-1] == '(' and string[i] == '('):
            stack.append(string[i])
        else:
            stack.pop()
    if not stack: 
        return True
    else: 
        return False

print(solution(p))