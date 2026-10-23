def get_Yaksoo(num):
    yak = []
    
    for i in range(1, num+1):
        if num % i == 0: yak.append(i)
    return yak

def solution(brown, yellow):
    answer = []
    check = get_Yaksoo(brown+yellow)
    
    if len(check)%2==0:
        y = len(check)//2 -1
        x = len(check)//2
    else:
        y = len(check)//2
        x = len(check)//2
    
    while y>=0 and x<len(check):
        if check[x]*check[y]==brown+yellow and (check[x]-2)*(check[y]-2)==yellow:
            return [check[x],check[y]]
        x+=1
        y-=1
    return answer