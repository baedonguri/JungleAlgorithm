from itertools import permutations
import sys

input = sys.stdin.readline

num = int(input())
arr = [list(map(int, input().split()))for i in range(num)]

n_num = [i for i in range(4)]

perm = list(permutations(n_num))

print(perm)
min_cost = 999999999
for p in perm:
    cost = []
    for i in range(num-1):
        cost.append(arr[p[i]][p[i+1]])
    cost.append(arr[p[-1]][p[0]])
        
    if 0 not in cost:
        min_cost = min(sum(cost),min_cost)

print(min_cost)