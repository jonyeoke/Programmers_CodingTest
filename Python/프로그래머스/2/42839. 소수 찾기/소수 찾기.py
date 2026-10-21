from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
    product,
)
def isPrime(num):
    for i in range(2, int(num**(0.5))+1):
        if num%i==0: return False
    return True


def solution(numbers):
    answer = 0
    
    all = []
    sets = set()
    for i in range(1, len(numbers)+1):
        all+=(list(permutations(numbers,i)))
    for now in all:
        now = int(''.join(now))
        sets.add(now)
    for now in sets:
        if int(now)==0 or int(now)==1: continue
        if isPrime(int(now)): answer+=1
        
    return answer