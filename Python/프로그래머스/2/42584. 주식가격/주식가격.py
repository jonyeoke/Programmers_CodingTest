def solution(prices):
    answer = [0] * len(prices)
    stk = []
    
    for i, price in enumerate(prices):
        
        while stk and stk[-1][1] > price:
            popped = stk.pop()
            j = popped[0]
            answer[j] = i-j
            
        stk.append((i,price))
        
    while stk:
        popped = stk.pop()
        j = popped[0]
        answer[j] = i-j
    return answer