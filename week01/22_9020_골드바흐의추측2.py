import sys
input = sys.stdin.readline

m = 10000
arr = [0,0] + [1] * (m-1)

# 에라토스테네스의 체
for i in range(2,int(m**0.5)+1):
    for j in range(i+i, m+1, i):
        if arr[i]: arr[j] = 0   

lst = []
for i in range(int(input())):
    n = int(input())
    # y가 소수이면서, n-x가 소수일 경우 리스트에 담음
    # 제일 마지막에 들어온 수가 차이가 제일 적기 때문에 리스트의 마지막을 출력
    prime = [[x, n-x] for x,y in enumerate(arr[:n//2+1]) if y and arr[n-x]][-1]
    print(*prime)

from itertools import com