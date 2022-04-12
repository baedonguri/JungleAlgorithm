import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)

    if n == 0:
        break

    stack = []
    max_area = 0

    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            max_area = max(max_area, width*arr[tmp])
        stack.append(i)
    while stack:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] -1
        max_area = max(max_area,width*arr[tmp]) 


    print(max_area)