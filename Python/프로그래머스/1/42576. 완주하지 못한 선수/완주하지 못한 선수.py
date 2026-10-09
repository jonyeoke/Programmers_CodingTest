def solution(participant, completion):
    answer = ''
    
    sp = sorted(participant)
    sc = sorted(completion)
    
    for i,now in enumerate(sc):
        if sp[i] != sc[i]:
            return sp[i]
    return sp[-1]
