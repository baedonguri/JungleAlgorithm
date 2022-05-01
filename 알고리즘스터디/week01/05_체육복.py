def solution(n,lost, reserve):
    answer = n-len(lost)
    visit = []

    for i in reserve:
        for j in lost:
            if i not in visit and j not in visit:
                if i+1 == j or i-1 == j:
                    print(j,i)
                    visit.append(i)
                    visit.append(j)
                    answer += 1

    return answer