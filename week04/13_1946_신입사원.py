import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    apply = [list(map(int, input().rstrip().split())) for _ in range(n)]
    apply.sort()

    cnt = 1
    Max = apply[0][1]

    for i in range(1,n):
        if Max > apply[i][1]:
            cnt += 1
            Max = apply[i][1]

    print(cnt)
