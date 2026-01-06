import heapq
def time_to_min(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour*60+minute

def solution(book_time):
    answer = 0
    book_time.sort(key= lambda x:x[0])
    rooms = []
    
    for start_str, end_str in book_time:
        start = time_to_min(start_str)
        end = time_to_min(end_str) + 10  
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        else:
            answer+=1
            
        heapq.heappush(rooms, end)
            
        
    return answer