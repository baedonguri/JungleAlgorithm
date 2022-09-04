n, m = '9881', '10724'
# n, m = '1','2'
smaller = len(m) if len(n) > len(m) else len(n)
dic = {
    1 : [0,1,1,0,0,0,0],
    2 : [1,1,0,1,1,0,1],
    3 : [1,1,1,1,0,0,1],
    4 : [0,1,1,0,0,1,1],
    5 : [1,0,1,1,0,1,1],
    6 : [1,0,1,1,1,1,1],
    7 : [1,1,1,0,0,1,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,1,1,0,1,1], 
    0 : [1,1,1,1,1,1,0],
}

print(smaller)
def calc_diff(x,y):
    return sum([1 for i,j in zip(x,y) if i!=j])
cnt = 0

for i, j in zip(n,m,-1):
    x,y = dic[int(i)], dic[int(j)]
    print(calc_diff(x,y))
    
    
# print(cnt)

# s = list(map(int, n))

# a,b = dic[n], dic[m]
# cnt = 0 
# for i,j in zip(a,b):
#     if i != j:
#         cnt += 1

# print(cnt)
