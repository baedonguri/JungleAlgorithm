import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int, input().split()))

start = 1 # 최소 톱날 높이 = 1m
end = max(trees) # 최대 톱날 높이 = 최대 나무 높이

while start <= end:
    mid = (start+end)//2 # 현재 톱날의 길이
    # total = 0 # 자른 나무들의 길이를 저장해둘 변수
    # for x in trees:
    #     if x > mid :
    #         total += x-mid
    # 나무들을 현재 톱날의 길이로 자른 후 남은 부분을 모두 더함
    total = sum([x-mid for x in trees if x>mid])

    # 만약 잘린 나무의 합이 m보다 작다면 톱날의 길이를 줄임
    if total < m:
        end = mid - 1
    else: # 크다면 톱날의 길이를 늘림
        result = mid # 최적값을 저장
        start = mid + 1
        
print(result)