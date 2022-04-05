import sys
input = sys.stdin.readline

nn = int(input())
kk = int(input())
arr = [input().strip() for i in range(nn)]

string = []
result = set()

def splice(arr, n):
    return arr[:n] + arr[n+1:]

def setCards(arr, k):
    global string
    n = len(arr)
    
    if k <= 0:
        result.add(''.join(string))
        return
        
    for i in range(n):
        string.append(arr[i])
        setCards(splice(arr,i), k-1)
        string.pop()
        

setCards(arr, kk)
print(len(result))