def solution(sequence, k):
    answer = []
    start = 0
    end = 0;
    now = sequence[start]
    min_length=10000001
    
    while start<=end:
        if now == k:
            if min_length>end-start:
                min_length = end-start
                answer=[start,end]
            now-=sequence[start]
            start+=1
        elif now<k:
            if end+1<=len(sequence)-1:
                end+=1
                now+=sequence[end]
            else:
                break
        else:
            now-=sequence[start]
            start+=1
            
    return answer