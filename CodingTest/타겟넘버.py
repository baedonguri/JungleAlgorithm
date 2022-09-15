# from itertools import product
# def solution(numbers, target):
#     arr = [(-n, n) for n in numbers]
#     answer = list(map(sum, product(*arr)))
#     return answer.count(target)


from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque()
    n = len(numbers)
    que.append([numbers[0], 0])
    que.append([-1*numbers[0], 0])
    
    while que:
        tmp, idx = que.popleft()
        if idx < n:
            que.append([tmp + numbers[idx], idx])
            que.append([tmp + -1*numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer
    
