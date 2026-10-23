from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    
    for i, now in enumerate(genres):
        d[now].append((i,plays[i]))
    
    for now in d:
        d[now].sort(key = lambda x: (-x[1], x[0]))
    
    d = sorted(d.items(), key= lambda x: sum(v[1] for v in x[1]), reverse=True)
    
    for now in d:
        for t in range(0, min(2, len(now[1]))):
            answer.append(now[1][t][0])
            
    return answer