def solution(phone_book):
    answer = True
    p = sorted(phone_book)
    
    for i in range(1, len(p)):
        if p[i].startswith(p[i-1]): return False
    
    
    return answer