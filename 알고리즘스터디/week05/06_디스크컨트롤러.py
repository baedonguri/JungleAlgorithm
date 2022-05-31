from heapq import heapify, heappush, heappop

jobs = [[0, 3], [1, 9], [2, 6]]	

heap = [[v,i] for i,v in jobs]
heapify(heap)

# answer = 0
# result = []
# now = heappop(heap)
# while heap:
#     next = heappop(heap)
#     if now[0] < next[1] < now[1]:
#         delay = now[0]-next[1]
#         next[0] += delay
#         next[1] += delay
#         answer += delay
#     else:
#         answer += now[0]-now[1]
#         now = next
    
#     result.append(answer)


#     print(answer)
# print(result)

# [3, 0]
# [6, 2]
# [9, 1]

answer = 0
while heap:
    now = heappop(heap)

    for next in heap:
        if now[0] > next[1]:
            

