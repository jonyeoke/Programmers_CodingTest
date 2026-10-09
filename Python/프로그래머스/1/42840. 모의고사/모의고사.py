def solution(answers):
    answer = []
    
    s1= (1,2,3,4,5)
    s2=(2, 1, 2, 3, 2, 4, 2, 5)
    s3=(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    
    correct=[0,0,0]
    
    for i in range(0,len(answers)):
        if answers[i] == s1[i%len(s1)]: correct[0]+=1
        if answers[i] == s2[i%len(s2)]: correct[1]+=1
        if answers[i] == s3[i%len(s3)]: correct[2]+=1
    max_one = max(x for x in correct)
    
    for i, now in enumerate(correct):
        if now==max_one: answer.append(i+1)
        
    return answer