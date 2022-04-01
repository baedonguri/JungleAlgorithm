def solution(arr):
    arr_len = len(arr)
    avg = sum(arr)/arr_len
    cnt = 0
    for score in  arr:
        if avg < score:
            cnt += 1
    result = (cnt/arr_len)*100
    
    return result

t = int(input())

for i in range(t):
    arr = arr = list(map(int,input().split()))
    avg = round(solution(arr[1:]), 3)
    
    print("{:.3f}%".format(avg))