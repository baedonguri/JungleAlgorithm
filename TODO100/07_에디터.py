# from collections import defaultdict
from sys import stdin
input = stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    command, *val = input().split()
    if command == 'P':
        left.append(val[0])
    elif command == 'L':
        if left:
            right.append(left.pop())
    elif command == 'D':
        if right:
            left.append(right.pop())
    elif command == 'B':
        if left:
            left.pop()
left.extend(reversed(right))
print("".join(left))

# string = input().rstrip()
# n = len(string)
# linked_list = defaultdict(list)
# tmp = [[i-1,i+1] for i in range(n-1)]
# for idx, val in enumerate(tmp): 
#     linked_list[idx] = val

# answer = list(string)
# cursor = len(answer)-1
# idx = len(answer)
# for i in range(int(input())):
#     command, *val = map(str, input().split())
#     if command == 'B':
#         if cursor == 0:
#             continue
#         del answer[cursor]
#         prev, next = linked_list[cursor-1]
#         linked_list[prev][1] = next
#         linked_list[next][0] = prev
#         cursor -= 1
#     elif command == 'P':
#         answer.insert(cursor, val)
#         prev, next = linked_list[cursor-1]
#         linked_list[idx] = [linked_list[prev][1],linked_list[next][0]]
#         linked_list[prev][1] = idx
#         linked_list[next][0] = idx
#         idx += 1
#         cursor += 1
#     else:
#         if command == 'L':
#             cursor -= 1
#             if cursor < 0: 
#                 cursor = len(answer)-1
#         elif command == 'D':
#             cursor += 1
#             if cursor > len(answer)-1:
#                 cursor = 0
        
#     print(answer, cursor)
    
                
