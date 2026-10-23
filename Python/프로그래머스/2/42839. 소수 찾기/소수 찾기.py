from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(0.5))+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = set()
    
    num = []
    cases = []
    for now in numbers:
        num.append(now)
    for i in range(1, len(numbers)+1):
        cases+=list(permutations(num,i))
    cases = list(set(cases))
    
    for now in cases:
        n = int(''.join(now))
        if isPrime(n): answer.add(n)
        
    return len(answer)