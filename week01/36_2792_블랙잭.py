n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_hap = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            hap = arr[i] + arr[j] + arr[k]
            if hap <= m and max_hap < hap:
                max_hap = hap
                
print(max_hap)