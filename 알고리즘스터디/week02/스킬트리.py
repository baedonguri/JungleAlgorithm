from collections import deque

# skill = "CBD"
# skill_trees	= ["BACDE", "CBADF", "AECB", "BDA"]	
# test = list("BDA")

# que = deque(skill)

# lst = []
# cnt = 0
# flag = True
# while que:
#     v = que.popleft()
#     for i in test:
#         if v == i: 
#             cnt += 1
#         else:
#             lst.append(i)
#         test.remove(i)
#     if v in lst:
#         flag = False
#         break
# print(flag)


def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        lst = list(skill)
        for s in skills:
            if s in skill and s != lst.pop(0):
                break
        
        else: answer += 1

    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))