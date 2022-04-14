import sys
input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# stack = []
# result = []
# for i in range(n):
#     stack.append(arr[i])
#     for j in range(i+1,n):
#         if stack[-1] < arr[j]:
#             result.append(arr[j])
#             stack.pop()
#             break
#     if stack:
#         result.append(-1)
#         stack.pop()

# print(*result)

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(answer)