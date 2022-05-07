def solution(board, moves):
    n = len(board)
    stack = []
    answer = 0
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                push_item = board[j][i-1]
                board[j][i-1] = 0
                
            if stack:
                if stack[-1] == push_item:
                    answer += 2
                    stack.pop()
                    break
            stack.append(push_item)
            break
    return answer