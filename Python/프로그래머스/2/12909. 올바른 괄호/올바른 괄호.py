def solution(s):
    stk = []
    
    for now in s:
        if now == '(':
            stk.append(now)
        else:
            if not stk:
                return False
            else:
                stk.pop()
    if stk:
        return False
    
    return True