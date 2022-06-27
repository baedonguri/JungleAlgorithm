# 투 포인터
# 각 배열에 입력 받는다.
# a와 b의 포인터를 생성하여 두 포인터가 각 배열의 끝이 아닐때 까지 진행한다.
# a포인터의 길이가 A배열의 끝에 다왔다면 B배열의 값을 추가한다.
# b포인터의 길이가 B배열의 끝에 다왔다면 A배열의 값을 추가한다.
# 두 배열의 길이가 끝이 아닌경우 각 배열의 포인터의 크기를 비교하여 더 작은 값을 넣어준다.
from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
pa,pb = 0,0
len_a, len_b = len(a), len(b)

while pa != len_a or pb != len_b:
    if pa == len_a:
        answer.append(b[pb])
        pb += 1
    elif pb == len_b:
        answer.append(a[pa])
        pa += 1
    else:
        if a[pa] < b[pb]:
            answer.append(a[pa])
            pa += 1
        else:
            answer.append(b[pb])
            pb += 1
print(*answer)