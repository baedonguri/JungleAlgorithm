import sys
input = sys.stdin.readline

def solve(n, board):
    total = sum([sum(i) for i in board])
    
    if total == 0:
        return print(0,end='')
    elif total == n*n:
        return print(1, end='')
    else:
        print('(',end='')
        tmp_board = [board[i][:n//2] for i in range(0,n//2)]
        solve(n//2, tmp_board)
        
        tmp_board = [board[i][n//2:] for i in range(0,n//2)]
        solve(n//2, tmp_board)
        
        tmp_board = [board[i][:n//2] for i in range(n//2,n)]
        solve(n//2, tmp_board)
        
        tmp_board = [board[i][n//2:] for i in range(n//2,n)]
        solve(n//2, tmp_board)
        
        print(')',end='')
        
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

solve(n,arr)