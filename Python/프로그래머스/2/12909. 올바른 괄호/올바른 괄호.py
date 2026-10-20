def solution(s):
    answer = True
    
    stk = []
    
    for now in s:
        if not stk:
            stk.append(now)
            continue
        if stk[-1]=='(':
            if now ==')':
                stk.pop()
            else:
                stk.append(now)
    
    if stk: return False

    return True