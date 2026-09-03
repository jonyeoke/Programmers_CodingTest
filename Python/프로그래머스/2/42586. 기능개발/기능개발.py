def solution(progresses, speeds):   
    answer = []
    left_days = []

    for i in range(len(progresses)):
        left_days.append((100 - progresses[i]) // speeds[i] + ((100 - progresses[i]) % speeds[i] > 0))
    
    now = left_days[0]
    count = 1
    for i in range(1, len(left_days)):
        if left_days[i] <= now:
            count += 1
        else:
            now = left_days[i]
            answer.append(count)
            count = 1
    
    answer.append(count)
    return answer