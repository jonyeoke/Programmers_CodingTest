def solution(s):
    answer = []
    list_ = s[2:-2].split('},{')
    list_= sorted(list_,key=lambda x:len(x))
    for i in list_:
        i = i.split(',')
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer