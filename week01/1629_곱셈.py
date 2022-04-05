import sys

input = sys.stdin.readline

def pow(a,b,m):
    if b == 1:
        return a%m
    
    val = pow(a,b//2,m)
    if b%2 == 0:
        return val
    
    return (val*val*a)%m

a,b,c = map(int, input().split())
result = pow(a,b,c)

print(result)