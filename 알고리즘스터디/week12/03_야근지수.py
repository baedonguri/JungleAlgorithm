import heapq
from collections import deque
from re import L
works = [1,1]
n = 3


def solution(n, works):
    answer = []

    if sum(works) < n:
        return 0
    for i in works:
        answer.append([-i,i])
    heapq.heapify(answer)
    
    for i in range(n):
        val = heapq.heappop(answer)
        val[0],val[1] = val[0]+1,val[1]-1
        heapq.heappush(answer, val)
    
    return sum([i[1]**2 for i in answer])




print(solution(n,works))
