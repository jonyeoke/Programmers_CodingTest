def solution(s):
    answer = ''
    save = []
    count=1
    for now in s:
        if now==" ":
            count=1
            save.append(' ')
            continue
        if count%2==1:
            save.append(now.upper())
        else:
            save.append(now.lower())
        count+=1
        
    return ''.join(save)