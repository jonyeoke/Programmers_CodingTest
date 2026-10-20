from collections import defaultdict

def solution(genres, plays):
    answer = []
    dicts = defaultdict(list)
    
    for i, now in enumerate(genres):
        dicts[now].append((i,plays[i]))
    sums = []
    
    for now in dicts:
        dicts[now] = sorted(dicts[now], key=lambda x: -x[1])
    
    for now in dicts:
        sums.append((now, sum(t[1] for t in dicts[now])))
    sums = sorted(sums, key=lambda x: -x[1])
    
    for now in sums:
        for i in range(0, min(len(dicts[now[0]]),2)):
            answer.append(dicts[now[0]][i][0])
    return answer