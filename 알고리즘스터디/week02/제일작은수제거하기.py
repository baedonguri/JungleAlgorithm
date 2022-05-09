def solution(arr):
    if len(arr) <= 1:
        arr[0] = -1
    else:
        min_idx = arr.index(min(arr))
        del arr[min_idx]
    return arr

print(solution([4,3,2,1]))
