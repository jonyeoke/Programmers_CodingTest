import math

def solution(n, stations, w):
    length=[]
    answer = 0
    before = -1
    
    for i, now in enumerate(stations):
        if i == 0:
            gap = now - w - 1
        else:
            gap = now - before - (2 * w) - 1

        if gap > 0:
            length.append(gap)

        before = now

    
    last_gap = n - stations[-1] - w
    if last_gap > 0:
        length.append(last_gap)
    
    for l in length:
        if l > 0:
            answer += math.ceil(l / (w*2+1))
    return answer