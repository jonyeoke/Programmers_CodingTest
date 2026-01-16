def solution(n):
    answer=0
    save=''
    now = n
    while int(now)>0:
        res = str(int(now)%3)
        now/=3
        save+=(res)

    cnt=len(save)-1
    for i in save:
        answer+=int(i)*(3**cnt)
        cnt-=1

    return answer