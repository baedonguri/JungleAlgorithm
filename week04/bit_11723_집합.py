import sys
input = sys.stdin.readline

m = int(input())
bit = 0
for _ in range(m):
    command, *num = input().split()

    if command == 'all':
        bit = (1<<20)-1
    elif command == 'empty':
        bit = 0
    else:
        num = int(num[0])-1
        if command == 'add':
            bit |= 1<<num
        elif command == 'remove':
            bit &= ~(1<<num)
        elif command == 'check':
            if bit & 1<<num:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            bit ^= 1<<num

