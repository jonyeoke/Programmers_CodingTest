def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for now in arr:
        if answer[-1]==now:
            continue
        answer.append(now)
    return answer