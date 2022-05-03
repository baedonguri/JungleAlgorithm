import sys
input = sys.stdin.readline

def search(target, book):
    start = 0
    end = len(book)-1

    while start <= end:
        mid = (start+end)//2

        if book[mid] == target:
            return 1
        elif book[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for _ in range(int(input())):
    n = int(input())
    book1 = list(map(int, input().split()))
    m = int(input())
    book2 = list(map(int, input().split()))

    book1.sort()

    for num in book2:
        print(search(num, book1))