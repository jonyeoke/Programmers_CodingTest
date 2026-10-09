from collections import defaultdict

def solution(tickets):
    answer = []
    used = [False]*len(tickets)
    
    ways = defaultdict(list)
    for src, dst in tickets:
        ways[src].append(dst)
    for key in ways:
        ways[key].sort()
    
    
    return ways
    
    return answer