def remove0(s):
    removed=''
    zeros=0
    for i in s:
        if i!='0':
            
            removed+=i
        else: zeros+=1
    return removed,zeros

def solution(s):
    result=[]
    cnt=0
    zeros=0
    now=s
    while now !='1':
        cnt+=1
        now,removed=remove0(now)
        now = bin(len(now))[2:]
        zeros+=removed
    
    result.append(cnt)
    result.append(zeros)
    return result
