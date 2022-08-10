from collections import defaultdict

def solution(N, stages):
    lst = defaultdict(list)
    players = len(stages)
    answer = []
    for i in stages:
        lst[i].append(i)

    for i in range(1,N+1):
        no_pass = len(lst[i])
        if not no_pass:
            answer.append([0,i])
            continue
        answer.append([no_pass/players, i])
        players -= no_pass
    
    answer = sorted(answer, key=lambda x : -x[0])

    return [i[1] for i in answer]


print(solution(4, [4,4,4,4,4]	))
