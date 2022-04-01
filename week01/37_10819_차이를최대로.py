from itertools import permutations

num = int(input())
arr = list(map(int, input().split()))
arr.sort()

arr = [i for i in permutations(arr)]

max_hap = 0
for lst in arr:
    hap = 0
    for i in range(0,num-1):
        hap += (abs(lst[i] - lst[i+1]))
    if hap > max_hap:
        max_hap = hap
        
print(max_hap)