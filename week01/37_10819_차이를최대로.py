import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_sum = 0
for p in permutations(arr):
    tmp_sum = 0
    for i in range(n-1):
        tmp_sum += abs(p[i]-p[i-1])
    if tmp_sum > max_sum:
        max_sum = tmp_sum

print(max_sum)