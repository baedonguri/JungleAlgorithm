arr = [int(input()) for i in range(9)]

max_num = arr[0]

for i in range(1,9):
    if max_num < arr[i]:
        max_num = arr[i]

max_idx = arr.index(max_num) + 1

print(max_num)
print(max_idx)