def consecutive_sum(start, end):
    if start == end:
        return start
    mid = (start+end)//2
    calc1 = consecutive_sum(start, mid)
    calc2 = consecutive_sum(mid+1, end)
    
    return  calc1 + calc2

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))