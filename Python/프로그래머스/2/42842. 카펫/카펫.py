def get_divisor_optimized(num):
    divisors = []
    root_num = int(num ** 0.5)
    for i in range(1, root_num + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    return sorted(list(set(divisors)),reverse=True)



def solution(brown, yellow):
    answer = []
    yaksu = get_divisor_optimized(brown+yellow)
    
    if len(yaksu)%2==0:
        i=(len(yaksu)//2)-1
        j = i+1
    else:
        i = j = len(yaksu)//2
    
    while i>=0 and j<=len(yaksu)-1:
        x = yaksu[i]
        y = yaksu[j]
        
        if x*y==brown+yellow and (x-2)*(y-2)==yellow:
            return [x,y]
        i-=1
        j+=1
    return yaksu
    return answer