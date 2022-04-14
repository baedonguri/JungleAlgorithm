import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]

def QuadTree(N, board):
    total = 0
    
    total = sum([sum(i) for i in board])
    
    if total == 0:
        print('0')
        return 0
    
    elif total == N*N:
        print('1')
        return 1
    else:
        print('(')
        temp = [board[i][0:N//2] for i in range(0,N//2)]
        QuadTree(N//2, temp)
        temp = [board[i][N//2:] for i in range(0,N//2)]
        QuadTree(N//2, temp)
        temp = [board[i][0:N//2] for i in range(N//2,N)] 
        QuadTree(N//2, temp)
        temp = [board[i][N//2:N] for i in range(N//2,N)]
        QuadTree(N//2, temp)
        print(')')

QuadTree(n, arr)