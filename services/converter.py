from datetime import datetime

month_dict = {1:'January',2: 'February',3:'March',4:'April',5:'May',
        6:'June',7:'July',8:'August',9:'September',10:'October',
        11:'November',12:'December'}
from services.parse_liquipedia import matches
actualy_matches = {'бла бла': 'July 10, 2023 - 2:12 UTC'}
def convert_mathes():
    global actualy_matches
    day = Convert_real_time.day()
    time = Convert_real_time.time()
    for i in matches.items():
        time_match = Convert_time_matches.int_time(i[1])
        day_match = Convert_time_matches.day(i[1])
        print('Вроде work')
        if int(day) < int(day_match):
            actualy_matches[i[0]] = i[1]
        elif int(day) == int(day_match) and int(time_match) >= int(time):
            actualy_matches[i[0]] = i[1]
        print(str(day),str(day_match))
        print(time,time_match)


class Convert_real_time():
    def day():
        day = str(datetime.now().date())[8:]
        if day[0] =='0':
            day = day[1:]
        return day
    def time():
        time = str(datetime.now().time())[:-10]
        str_time = ''
        if time[0] == '0':
            time = time[1:]
        for i in time.split(':'):
            str_time += i
        return int(str_time)
    def month():
        month = str(datetime.now().date())[5:7]
        if month[0] == '0':
            month = month[1:]
        return month
    def year():
        year = str(datetime.now().date())[0:4]



class Convert_time_matches():
    def start(match):
        datetime_match = match.replace(',','').replace('-','')
        datetime_match: list = datetime_match.split()
        return datetime_match


    def is_hour_over_24_for_day(match):
        is_day = False
        list_time = Convert_time_matches.str_time(match).split(':')
        if int(list_time[0]) >= 24:
            is_day =True
        return is_day


    def if_hour_over_24_for_time(time):
        list_time :list[str] = time.split(':')
        str_time = ''
        if int(list_time[0]) >= 24:
            list_time[0] -= 24
        for i in list_time:
            str_time += i +':'
        return str_time


    def str_time(match):
        time_match = ''
        datetime_match = Convert_time_matches.start(match)
        times_match = datetime_match[3].split(':')
        times_match[0] = int(times_match[0]) + 6
        for i in times_match:
            time_match += str(i) + ':'
        time_match= Convert_time_matches.if_hour_over_24_for_time(time_match[:-1])
        return time_match[:-1]


    def int_time(match):
        str_time = Convert_time_matches.str_time(match)
        list_time = str_time.split(':')
        int_time = int(list_time[0] + list_time[1])
        return int_time


    def day(match):
        datetime_match = Convert_time_matches.start(match)
        day = int(datetime_match[1])
        if Convert_time_matches.is_hour_over_24_for_day(match):
            dat +=1
        return day

for i in matches.items():
    print(Convert_time_matches.str_time(i[1])+'.'+str(Convert_time_matches.day(i[1])))
    print(Convert_time_matches.int_time(i[1]))
print(datetime.now().date())
print(datetime.now().time())