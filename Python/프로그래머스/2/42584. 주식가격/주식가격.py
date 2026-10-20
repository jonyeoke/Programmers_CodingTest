def solution(prices):
    answer = [0]*len(prices)
    
    stk = []
    for i, now in enumerate(prices):
        while stk and stk[-1][0] > now:
            popped, j = stk.pop()
            answer[j] = i-j
        stk.append((now,i))
    while stk:
        now, i = stk.pop()
        answer[i] = len(prices)-i-1
    return answer