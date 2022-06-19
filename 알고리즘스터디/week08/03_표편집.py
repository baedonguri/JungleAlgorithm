# 프로그래머스 표 편집
# 실패

n = 8
k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	

# def solution(n,k,cmd):
#     check = ['O']*n
#     backing_store = []
 
#     cur_idx = k
#     for command in cmd:
#         if command.startswith('D'):
#             cur_idx += int(command.split(' ')[1])
#         elif command.startswith('U'):
#             cur_idx -= int(command.split(' ')[1])
#         elif command == 'C':
#             check[cur_idx] = 'X'
#             backing_store.append(cur_idx)
#             cur_idx += 1
#         else:
#             re_idx = backing_store.pop()
#             check[re_idx] = 'O'
#     return "".join(check)

def solution(n,k,cmd):
    check = ['O']*n
    linked_list = {i:[i-1,i+1] for i in range(1, n+1)}
    backing_store = []
    cur_idx = k+1
    for command in cmd:
        if command.startswith('D'):
            cur_idx = linked_list[cur_idx][1]
        elif command.startswith('U'):
            cur_idx = linked_list[cur_idx][0]
        elif command == 'C':
            prev,next = linked_list[cur_idx]
            backing_store.append([prev,next,cur_idx])
            check[cur_idx-1] = 'X'

            if next == n+1:
                cur_idx = linked_list[cur_idx][0]
            else:
                cur_idx = linked_list[cur_idx][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next
        else:
            prev,next,now = backing_store.pop()
            check[now-1] = 'O'

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(check)


            
    



print(solution(n,k,cmd))

