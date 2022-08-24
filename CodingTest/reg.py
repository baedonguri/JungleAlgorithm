# 정규표현식 사용하기
from collections import defaultdict
from email.policy import default
import re



# 1-1 문자열 판단하기
# print(re.match('Hello', 'Hello world!'))
# print(re.match('Python', 'Hello world!'))

# 1-2 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
# print(re.search('^Hello', 'Hello, world!')) # Hello로 시작하므로 패턴에 매칭됨
# print(re.search('world!$', 'Hello, world!')) # world!로 끝나므로 매칭

# 1-3 지정된 문자열이 하나라도 포함되는지 확인하기
# print(re.match('hello|world', 'world'))

# 4 문자열 바꾸기
# reg1 = re.sub('apple|orange', 'fruit', 'apple box orange tree')
# print(reg1)

# reg2 = re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')
# print(reg2)

# def multiple10(m):
#     n = int(m.group())
#     return str(n * 10)

# reg3 = re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')
# print(reg3)

# reg4 = re.sub('[0-9]+', lambda m : str(int(m.group())*10), '1 2 Fizz 4 Buzz Fizz 7 8')
# print(reg4)

# print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-4444-5555'))
# print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '010-227-2282'))


# print(re.findall('[A-Za-z]+', '1 2 Fizz 4 Buzz Fizz 7 8'))

# print(re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234'))

# print(re.sub('({\s*)"(\w+)" : \s*"(\w+)"(\s*})', '<\\2>\\3<\\2>', '{ "name" : "james" }'))

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
text = "Does [ prime_first_b, prime_first_a] [ amazone_first_a, prime_first_a] [ google_first_a] show me the money"
dic = defaultdict(list)

arr = re.findall('\[(.*?)\]', text)
cnt = 1
for i in arr:
    sub_string = i.split(',')
    for string in sub_string:
        if string not in dic:
            dic[string] = cnt
            cnt += 1

print(re.sub('\[(.*?)\]', ))