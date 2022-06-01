from itertools import combinations
from collections import Counter

def check(s, string):
    box = ""
    for i in list(s):
        if i in string:
            box += i 
    return box


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ","ACD"]
course = [2,3,4]


# def solution(orders, course):
#     answer = defaultdict(list)
#     orders.sort(key=lambda x:len(x))
#     for i in range(len(orders)):
#         cnt = 0
#         for j in range(i, len(orders)):
#             if check(orders[i], orders[j]):
#                 cnt += 1
#         answer[orders[i]] = cnt
        
#     result = []

#     for i in answer:
#         if answer[i] in course:
#             result.append(i)
#     result.sort()
#     return result

def solution(orders, course):
    answer = []
    for num in course:
        arr = []
        for order in orders:
            order = sorted(order)
            arr.extend(list(combinations(order,num)))
        count = Counter(arr)

        if count:
            if max(count.values()) >= 2:
                for key, val in count.items():
                    if val == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)
print(solution(orders, course))
