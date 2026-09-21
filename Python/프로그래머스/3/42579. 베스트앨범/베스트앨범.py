from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    counter = defaultdict(int)
    best = defaultdict(list)
    
    for i, (now_g, now_p) in enumerate(zip(genres,plays)):
        counter[now_g] += now_p
        best[now_g].append((now_p,i))
    
    sorted_counter = sorted(counter.items(), key=lambda x:-x[1])
    
    for g, c in sorted_counter:
        sorted_best = sorted(best[g], key=lambda x: (-x[0], x[1]))
        for play, idx in sorted_best[:2]:
            answer.append(idx)
    return answer