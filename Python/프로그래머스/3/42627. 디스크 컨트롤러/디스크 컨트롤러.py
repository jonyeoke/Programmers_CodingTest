import heapq

def solution(jobs):
    answer = 0
    h = []

    finished = 0
    jobs = sorted(jobs, key=lambda x: x[0])

    now = 0
    i = 0

    while finished < len(jobs):
        while i < len(jobs) and jobs[i][0] <= now:
            heapq.heappush(h, (jobs[i][1], jobs[i][0], i))
            i += 1

        if h:
            l, s, idx = heapq.heappop(h)
            now += l
            answer += now - s
            finished += 1
        else:
            now = jobs[i][0]

    return answer // len(jobs)
