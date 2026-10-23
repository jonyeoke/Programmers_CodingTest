def solution(participant, completion):
    answer = ''
    p = sorted(participant)
    c = sorted(completion)
    
    for i, nc in enumerate(c):
        if nc != p[i]:
            return p[i]
    return p[-1]