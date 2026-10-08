def solution(s):
    stk = []

    for now in s:
        if now == ')':
            if not stk:
                return False
            stk.pop()
        else:
            stk.append(now)

    if stk:
        return False

    return True