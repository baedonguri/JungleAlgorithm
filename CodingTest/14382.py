from sys import stdin
input = stdin.readline
t = int(input().rstrip())
def ntos(n):
    n_lst = list(map(int, str(n)))
    for num in n_lst:
        if not check[num]:
            check[num] = True

for i in range(t):
    n = int(input().rstrip())
    check = [False]*10
    if n == 0:
        print('Case #' + str(i + 1) + ': INSOMNIA')
        continue        
    j = 0
    while True:
        value = (j+1) * n
        ntos(value)
        if all(check): 
            print('Case #' + str(i+1) + ': ' + str(value))
            break
        j += 1