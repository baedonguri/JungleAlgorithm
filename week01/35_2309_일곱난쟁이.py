n = 9

arr = [int(input()) for i in range(n)]

total = sum(arr)

for i in range(n):
    for j in range(i+1,n):
        if total-arr[i]-arr[j] == 100:
            tmp1,tmp2 = arr[i], arr[j]

arr.remove(tmp1)
arr.remove(tmp2)
arr.sort()

for i in arr:
    print(i)