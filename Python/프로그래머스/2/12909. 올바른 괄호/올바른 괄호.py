def solution(s):
    answer = True
    
    stk = []
    
    for now in s:
        if not stk:
            if now == '(': 
                stk.append(now)
                continue
            else: return False
        if now == '(':
            stk.append(now)
        else:
            if stk[-1] == '(':
                stk.pop()
    if stk: return False
    return True