def solution(answers):
    answer = []
    record = [0,0,0]
    i=0
    j=0
    k=0
    
    p1 = [1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for now in answers:
        if p1[i]==now:
            record[0]+=1
        if p2[j]==now:
            record[1]+=1
        if p3[k]==now:
            record[2]+=1
        
        i = (i+1)%len(p1)
        j = (j+1)%len(p2)
        k = (k+1)%len(p3)
    for i, rcd in enumerate(record):
        if rcd == max(record):
            answer.append(i+1)
    return answer