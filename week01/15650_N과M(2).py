import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = []

def func(s):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(s, n+1):
        if i not in lst:
            lst.append(i)
            func(s+1)
            lst.pop()
            
func(1)