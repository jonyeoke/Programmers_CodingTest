def solution(phone_book):
    answer = True
    phone_book=sorted(phone_book)
    
    for i, now in enumerate(phone_book):
        if i<len(phone_book)-1:
            if phone_book[i+1].startswith(now)>0:
                return False
        
    
    return answer