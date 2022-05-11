def make_set(string):
    n = len(string)
    tmp_set = []
    string = string.lower()
    for i in range(n-1):
        if string[i].isalpha() and string[i+1].isalpha():
            tmp = "".join((string[i],string[i+1]))
            tmp_set.append(tmp)
    return sorted(tmp_set)

def solution(str1, str2):
    str1 = make_set(str1)
    str2 = make_set(str2)

    if len(str1) > len(str2):
        inter = [str1.remove(x) for x in str2 if x in str1]
    else:
        inter = [str2.remove(x) for x in str1 if x in str2]

    lst_union = str1 + str2
    uni = len(lst_union)

    if not uni: return 65536
    
    return int(len(inter)/uni*65536)
    
print(solution('handshake', 'handshake'))