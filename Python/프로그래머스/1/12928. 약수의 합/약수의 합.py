def solution(n):
    answer = 0
    
    start = 1
    
    while(start<=n):
        if(n%start==0):
            answer+=start
        start+=1
    
    return answer