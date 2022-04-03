import sys
input = sys.stdin.readline

n = 10000
arr = [True] * n
m = int(n**0.5)

for i in range(2,m+1):
    if arr[i] == True:
        for j in range(i+i,n,i):
            arr[j] = False
            
arr =  [i for i in range(2,n) if arr[i] == True]

num = int(input())

for _ in range(num):
    p_num = int(input())
    result = []
    
    for i in range(p_num):
        for j in range(p_num):
            if arr[i] + arr[j] == p_num:
                result.append([arr[i],arr[j]])
    
    result = sorted(result, key=lambda x : abs(x[0]-x[1]))
    r,c = result[0][0],result[0][1]
    print(r, end=' ')
    print(c)