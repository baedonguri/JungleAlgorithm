from bisect import bisect_left, bisect_right
from sys import stdin

input = stdin.readline

def find_card_amount(x):
    first = bisect_left(arr, x)
    end = bisect_right(arr, x)
    return end - first

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
find = list(map(int, input().split()))

arr.sort()

for i in find:
    print(find_card_amount(i),end=' ')