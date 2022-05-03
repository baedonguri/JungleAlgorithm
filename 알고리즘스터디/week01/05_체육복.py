# def solution(n,lost, reserve):
#     answer = n-len(lost)
#     visit = []

#     for i in reserve:
#         for j in lost:
#             if i not in visit and j not in visit:
#                 if i+1 == j or i-1 == j:
#                     print(j,i)
#                     visit.append(i)
#                     visit.append(j)
#                     answer += 1

#     return answer


from collections import deque

def solution(n,lost, reserve):
    answer = n - len(lost)
    s_reserve = set(reserve)-set(lost)
    s_lost = set(lost)-set(reserve)
    
    que = deque(s_lost)
    
    while que:
        l_num = que.popleft()
        for r_num in s_reserve:
            if l_num+1 == r_num or l_num-1 == r_num:
                answer += 1
                s_reserve.remove(r_num)
                break

    return answer


n = 5
lost = [2,4]
reserve = [1,3,5]

print(solution(n,lost,reserve))