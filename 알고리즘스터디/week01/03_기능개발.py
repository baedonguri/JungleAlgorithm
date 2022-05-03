from math import ceil
from collections import deque


def solution(progresses, speeds):
    arr = []
    answer = []
    idx = 0

    for p, s in zip(progresses, speeds):
        arr.append(ceil((100-p)//s))
    
    print(arr)
    for i in range(len(arr)):
        if arr[idx] < arr[i]:
            answer.append(i-idx)
            idx = i

    answer.append(len(arr)-idx)

    return answer

# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([96,94],[3,3]))