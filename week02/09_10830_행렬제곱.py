import sys
input = sys.stdin.readline

def mat_mul(a,b):
    n = len(a)
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[i][j] += a[i][k]*b[k][j]
    mat_div(arr)
    return arr

def mat_div(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            arr[i][j] %= 1000
            
def dnq(a,b):
    if b == 1:
        return a
    x = dnq(a,b//2)
    if b%2: 
        return mat_mul(mat_mul(x,x), a)
    else: 
        return mat_mul(x,x)
    
N,B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
mat_div(matrix)
print("\n".join(map(lambda x: " ".join(map(str, x)), dnq(matrix, B))))