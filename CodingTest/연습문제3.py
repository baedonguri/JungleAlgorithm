from collections import defaultdict
def solution(invitationPairs):
    dic = defaultdict(list)
    
    for pair in invitationPairs:
        invitation, invited = pair
        if invitation not in dic:
            dic[invitation] = [0,[]]
        dic[invitation][0] += 1
        dic[invitation][1].append(invited)

    score = defaultdict(list)
    for key, value in dic.items():
        score[key] = value[0] * 10
        for i in value[1]:
            if i in dic:
                inviter1 = dic[i]
                score[key] += inviter1[0] * 3
                for j in inviter1[1]:
                    if j in dic:
                        inviter2 = dic[j]
                        score[key] += inviter2[0] * 1

    answer = sorted(score.items(), key= lambda x:x[1], reverse=True)[:3]

    return [i[0] for i in answer]