def solution(numbers):
    answer = []
    for i in numbers:
        bin_num = list('0'+bin(i)[2:])
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'
        
        if i%2:
            bin_num[idx+1] = '0'
            
        answer.append(int(''.join(bin_num),2))
        
    return answer