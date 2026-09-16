def solution(s):
    answer = []
    check = False
    for i, now in enumerate(s):
        if i==0:
            if not now.isdigit():
                answer.append(now.upper())
            else: answer.append(now)
        elif now == ' ':
            check = True
            answer.append(now)
        elif check:
            answer.append(now.upper())
            check=False
        elif now.isupper():
            answer.append(now.lower())
        else:
            answer.append(now)
            
    result = "".join(answer)
    
    return result