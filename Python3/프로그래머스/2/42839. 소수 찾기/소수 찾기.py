import itertools

def is_Prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numberset = set()
    
    for i in range(1, len(numbers) + 1):
        perm_list = itertools.permutations(numbers, i)
        
        for perm in perm_list:
            num = int("".join(perm))
            numberset.add(num)
    numberset = list(numberset)

    answer = 0
    for num in numberset:
        if is_Prime(num):
            answer+=1
    return answer