import re

def solution(phone_number):
    answer = ''
    lentoset=len(phone_number)-4
    answer =  re.sub(r'\d(?=\d{4})','*',phone_number)
    return answer