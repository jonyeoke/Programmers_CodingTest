def solution(n, lost, reserve):
    answer = 0
    
    got = [True]*n
    
    for check in lost:
        got[check-1]=False
    for now in lost[:]:
        if now in reserve:
            got[now - 1] = True
            lost.remove(now)
            reserve.remove(now)
    reserve = sorted(reserve)
    for now in reserve:
        if now > 1 and got[now-2] == False:
            got[now-2] = True
        elif now < n and got[now] == False:
            got[now] = True
    
    for now in got:
        if now: answer+=1
    return answer