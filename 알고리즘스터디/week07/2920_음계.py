# arr = list(map(int, input().split()))
# if ("".join(map(str, arr)) == "12345678"):
#     print("acscending")
# elif ("".join(map(str, arr)) == "87654321"):
#     print("descending")
# else:
#     print("mixed")


from sys import stdin
input = stdin.readline
arr = list(map(int, input().rstrip().split()))

def solution(arr):
    start = arr[0]
    if start == 8:
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]+1:
                return "mixed"
        return 'descending'           
    else:
        for i in range(len(arr)-1):
            if arr[i]+1 != arr[i+1]:
                return "mixed"
        return "ascending"

print(solution(arr))