from functools import cmp_to_key
from itertools import permutations

def cmp(a, b):
    
    if a+b>b+a:
        return 1
    elif a+b<b+a:
        return -1
    else:
        return 0

def solution(numbers):
    answer = ''
    n = [str(x) for x in numbers]
    
    n = sorted(n, key=cmp_to_key(cmp),reverse=True)
    answer = ''.join(n)
    if answer[0]=='0': return '0'
    return answer