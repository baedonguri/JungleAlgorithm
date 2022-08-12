def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)

    for i in range(n):
        index = n-i
        
        if citations[i] >= index:
            answer = index
            break

    return answer


print(solution([3,9,6,1,5]))