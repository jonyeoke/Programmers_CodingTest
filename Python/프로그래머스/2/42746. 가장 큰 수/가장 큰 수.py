from functools import cmp_to_key

def cmp(a, b):
    a = str(a)
    b = str(b)
    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1
    else:
        return 0

def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=cmp_to_key(cmp))
    if int(numbers[0])==0:
        return '0'
    answer = "".join(str(x) for x in numbers)
    
    return answer