def solution(prices):
    answer = [0]*len(prices)
    
    stk=[]
    
    for i, now in enumerate(prices):
        while stk and now < stk[-1][0]:
            _, n = stk.pop()
            answer[n] = i-n
        stk.append((now,i))
    while stk:
        _,n=stk.pop()
        answer[n]=len(prices)-n-1
    
    return answer