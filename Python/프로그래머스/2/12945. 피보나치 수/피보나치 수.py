def solution(n):
    answer = 0
    
    save=[0,1]
    
    for now in range(2,n+1):
        if now%2==0:
            answer = (save[0]+save[1])%1234567
            save[0]=answer
        else:
            answer = (save[0]+save[1])%1234567
            save[1]=answer
    return answer