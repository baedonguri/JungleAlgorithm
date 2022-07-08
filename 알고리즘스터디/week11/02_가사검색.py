from bisect import bisect_left, bisect_right
import collections

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries	= ["fro??", "????o", "fr???", "fro???", "pro?"]

def Counter(a,left,right):
    left_idx = bisect_left(a, left)
    right_idx = bisect_right(a, right)
    
    return right_idx-left_idx

def solution(words, queries):
    answer = []
    dic = collections.defaultdict(list)
    re_dic= collections.defaultdict(list)

    for word in words:
        dic[len(word)].append(word)
        re_dic[len(word)].append(word[::-1])

    for key in dic.keys():
        dic[key].sort()
        re_dic[key].sort()
    
    for key in dic.values():
        print(key)

    for query in queries:
        if query[0] == '?':
            query = query[::-1]
            my_query = re_dic[len(query)]
            first = query.replace('?','a')
            last = query.replace('?', 'z')
            answer.append(Counter(my_query, first, last))
        else:
            my_query = dic[len(query)]
            first = query.replace('?','a')
            last = query.replace('?', 'z')
            answer.append(Counter(my_query,first,last))
    return answer
print(solution(words, queries))