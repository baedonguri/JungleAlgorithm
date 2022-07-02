from sys import stdin
input = stdin.readline
# n, k = map(int, input().split())

# arr = []
# bit = 1
# for i in range(n):
#     word = list(input().rstrip())[4:-4]
#     print(word)

# print(set(arr))



def check_bit(b):
    num = ord(b)-97
    return (1<<num)

print(check_bit('b'))


