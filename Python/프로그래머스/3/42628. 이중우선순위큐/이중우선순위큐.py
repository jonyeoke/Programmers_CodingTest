from collections import defaultdict
import heapq
def solution(operations):
    answer = []
    mn = []
    mx = []
    cnt = defaultdict(int)
    
    for now in operations:
        cmd, num = now.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(mn,num)
            heapq.heappush(mx,-num)
            cnt[num]+=1
        else:
            if num>0:
                while mx and cnt[-mx[0]]==0:
                    popped = -heapq.heappop(mx)
                
            else:
                while mn and cnt[mn[0]]==0:
                    popped = heapq.heappop(mn)
    return answer



from collections import defaultdict
import heapq

def solution(operations):
    mn = []
    mx = []
    cnt = defaultdict(int)

    for now in operations:
        cmd, num = now.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(mn, num)
            heapq.heappush(mx, -num)
            cnt[num] += 1

        else:
            if num == 1:
                while mx and cnt[-mx[0]] == 0:
                    heapq.heappop(mx)

                if mx:
                    val = -heapq.heappop(mx)
                    cnt[val] -= 1

            else:
                while mn and cnt[mn[0]] == 0:
                    heapq.heappop(mn)

                if mn:
                    val = heapq.heappop(mn)
                    cnt[val] -= 1

    while mx and cnt[-mx[0]] == 0:
        heapq.heappop(mx)

    while mn and cnt[mn[0]] == 0:
        heapq.heappop(mn)

    if not mx or not mn:
        return [0, 0]

    return [-mx[0], mn[0]]
