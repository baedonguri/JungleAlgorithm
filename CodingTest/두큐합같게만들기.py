from collections import deque
def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)    
    sum_q1 = sum(que1)
    sum_q2 = sum(que2)
    
    i = 0
    while i <= 600000:
        if sum_q1 == sum_q2:
            return i
        elif sum_q1 > sum_q2:
            num = que1.popleft()
            que2.append(num)
            sum_q1 -= num
            sum_q2 += num
        else:
            num = que2.popleft()
            que1.append(num)
            sum_q2 -= num
            sum_q1 += num
        i += 1
    return -1