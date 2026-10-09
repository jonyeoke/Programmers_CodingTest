def isPrime(num):
    if num==0 or num==1: return False
    for i in range(2,int((num)**(0.5))+1):
        if num % i==0: return False
    
    return True

def dfs(now, numbers, nset, visited):
    if isPrime(int(now)):
        nset.add(int(now))
    for i, n in enumerate(numbers):
        if visited[i]==True: continue
        visited[i]=True
        nset = dfs(now+n,numbers,nset,visited)
        visited[i]=False
    
    return nset

def solution(numbers):
    answer = 0
    numl=[]
    visited = [False]*len(numbers)
    nset=set()
    for i, n in enumerate(numbers):
        
        if n=='0': continue
        visited[i]=True
        nset = dfs(n,numbers,nset,visited)
        visited[i]=False
    return len(nset)