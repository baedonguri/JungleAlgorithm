from itertools import combinations
from collections import defaultdict
import bisect
def solution(infos, query):
    query = [i.replace('and','').split() for i in query]
    infos = [i.split() for i in infos]

    info_dict = defaultdict(list)

    for info in infos:
        for i in range(5):
            for j in combinations(info[:-1],i):
                info_dict[''.join(j)].append(int(info[-1])) 

    for i in info_dict:
        info_dict[i].sort()

    answer = []

    for i in query:
        score = int(i[-1])
        result = ''.join(i[:-1]).replace('-','')
        ans = info_dict[result]
        answer.append(len(ans)-bisect.bisect_left(ans,score))

    return answer