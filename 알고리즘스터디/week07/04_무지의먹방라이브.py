from collections import deque
import heapq

food_times = [3,1,2]
k = 5
# def solution(food_times, k):
#     arr = list(enumerate(food_times))
#     que = deque(arr)
#     time = 0
#     while True:
#         e_time = list(que.popleft())
#         if e_time[1] == 0:
#             while True:
#                 que.append(e_time)
#                 e_time = list(que.popleft())
#                 if e_time[1] != 0:
#                     break
#         e_time[1] -= 1
#         time += 1
#         que.append(e_time)
#         if time == k:
#             break
#     if any(i[1]>0 for i in que):
#         return que.popleft()[0]+1
#     return -1


def solution(food_times, k):
    answer = -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))

    food_num = len(food_times) # 남은 음식 갯수
    pre = 0
    while heap:
        t = (heap[0][0] - pre) * food_num
        if k >= t:
            k -= t
            pre, _ = heapq.heappop(heap)
            food_num -= 1
        else:
            idx = k%food_num
            heap.sort(key=lambda x:x[1])
            answer = heap[idx][1]
            break
    return answer



print(solution(food_times,k))
