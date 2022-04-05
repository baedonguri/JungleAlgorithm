from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
arr = [input().strip() for i in range(n)]
perm = [i for i in permutations(arr,k)]
result = []

for i in perm:
    result.append("".join(i))

result = list(set(result))

print(len(result))