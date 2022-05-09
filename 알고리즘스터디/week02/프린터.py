from collections import deque

def solution(priorities,location):
    que = deque([(idx, val) for idx, val in enumerate(priorities)])
    
    answer = 0
    while True:
        v = que.popleft()
        if any(v[1] < q[1]for q in que):
            que.append(v)
        else:
            answer += 1
            if v[0] == location:
                break
    return answer

    

print(solution([2, 1, 3, 2],2))