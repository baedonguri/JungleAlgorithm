import sys
input = sys.stdin.readline
def fact(n):
    if n <= 1:
        return 1
    return n *fact(n-1)

result = fact(int(input()))
print(result)