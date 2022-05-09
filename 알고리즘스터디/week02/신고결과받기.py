from collections import defaultdict
def solution(id_list, report, k):

    report = list(set(report))
    r_dic,u_dic = defaultdict(list), defaultdict(list)
    answer = []
    
    # 1.1 각 유저별로 신고 당한 횟수를 기록
    for rep in report:
        x,y = rep.split(" ")
        
        if y not in r_dic: 
            r_dic[y] = 1
        else: 
            r_dic[y] += 1
        u_dic[x] += [y] # 1.2 유저별 신고한 대상을 저장
    
    # 2.1 전체 유저 리스트 순회
    for u_id in id_list:
        cnt = 0
        # 2.2 해당 유저가 신고한 녀석들을 확인
        for v in u_dic[u_id]:
            # 2.3 정지되었다면 + 1
            if r_dic[v] >= k: 
                cnt += 1
        # 최종적으로 날릴 메일의 갯수
        answer.append(cnt)

    return answer