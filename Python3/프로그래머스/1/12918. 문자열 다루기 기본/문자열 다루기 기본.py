import re

def solution(s):
    answer = False
    if (len(s)==4 or len(s)==6) and bool(re.match(r'^[0-9]+[0-9]$',s)): answer = True
    
    return answer
    