def get_remain_time(progress, speed):
    now = progress
    time = 0
    
    while now<100:
        now+=speed
        time+=1
    return time

def solution(progresses, speeds):   
    answer = []
    
    times = []
    
    for i, now in enumerate(progresses):
        times.append(get_remain_time(now, speeds[i]))
    
    i = 1
    nums = 1
    now = times[0]
    
    while i < len(times):
        if now<times[i]:
            answer.append(nums)
            now = times[i]
            nums=1
        else:
            nums+=1
        i+=1
    answer.append(nums)
    
    return answer