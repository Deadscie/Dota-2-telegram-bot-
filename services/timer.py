from datetime import datetime
from services.converter import Convert_real_time,Convert_time_matches,actualy_matches

count = 0

def timer():
    global count
    list_matches = []
    time = Convert_real_time.time()
    day = Convert_real_time.day()
    list_matches = list(actualy_matches.items())
    i = list_matches[count]
    time_match = Convert_time_matches.int_time(i[1])
    day_match = Convert_time_matches.day(i[1])
    count += 1
    if count > len(list_matches)-1:
        count = 0
    if int(day_match) == int(day) and time == time_match:
        return i[0]
    print(day_match,' - ',day, ' ' ,day_match == day)
    print(time,' - ',time_match, ' ' ,time == time_match)
    return False
