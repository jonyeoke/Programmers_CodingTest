def recursive(num,count):
    if count>=500: return -1
    if num==1: return count
    elif num%2==0: return recursive(num/2,count+1)
    else: return recursive(num*3+1,count+1)
def solution(n):
    return recursive(n,0)