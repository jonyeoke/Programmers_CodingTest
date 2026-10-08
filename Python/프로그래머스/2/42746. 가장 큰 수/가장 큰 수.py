from functools import cmp_to_key

def cmp(num1, num2):
    if str(num1)+str(num2)<str(num2)+str(num1):
        return 1
    else : return -1

def solution(numbers):
    answer = ''
    
    numbers=sorted(numbers, key=cmp_to_key(cmp))
    
    if numbers[0]==0: return '0'
    
    return ''.join(map(str,numbers))