from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    ways = list(permutations(dungeons))
    
    for now in ways:
        left = k
        record = 0
        for n in now:
            if left >= n[0]:
                record+=1
                left-=n[1]
            else:
                break
        answer = max(answer,record)
        
    return answer