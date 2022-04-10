import sys
input = sys.stdin.readline
arr = []

for i in range(int(input())):
    n = int(input())
    if n != 0:
        arr.append(n)
    if len(arr) != 0 and n == 0:
        arr.pop()
        
print(sum(arr))