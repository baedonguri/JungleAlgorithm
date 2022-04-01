import sys
def fsort(a,max_):
    n = len(a)
    f = [0] * (max_ + 1)
    b = [0] * n
    
    for i in range(n):
        f[a[i]] += 1
    for i in range(1,max_ + 1):
        f[i] += f[i-1]
    for i in range(n-1,-1,-1):    
        f[arr[i]] -= 1
        b[f[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = b[i]

num = int(sys.stdin.readline())
arr = []
for i in range(num):
    arr.append(int(sys.stdin.readline()))
    
fsort(arr, max(arr))

for i in arr:
    print(i)