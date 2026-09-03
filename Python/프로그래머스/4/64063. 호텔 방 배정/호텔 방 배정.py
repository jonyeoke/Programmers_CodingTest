import sys
sys.setrecursionlimit(1000000)

def find_empty_room(node, rooms):
    if node not in rooms:
        rooms[node] = node + 1
        return node
    empty_room = find_empty_room(rooms[node], rooms)
    rooms[node] = empty_room + 1
    return empty_room

def solution(k, room_number):
    answer = []
    rooms = {}
    
    for num in room_number:
        assigned = find_empty_room(num, rooms)
        answer.append(assigned)
        
    return answer