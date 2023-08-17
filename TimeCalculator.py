# The following will provide time calculation
# via the function add_time
# it will not use any modules




# functions
#  main function : add_time
# hour_to_minute - translate the time to minutes
# eval_day - returns the current day after time add
#new_day_of_week -

''' n days: I will turn  the  2 entered value into minutes
add between them divide by 24 * 60 a figure out number of days passed

new time: turn back the minutes into hours by using modulo 24 * 60  '''
MIN_A_DAY = 24 * 60
space = ' '
days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
values = list(range(0, 7))
d = dict(zip(values , days_list))



# return hours to min
def hour_to_min(value):

    idx = value.find('AM')
    if idx == -1:
        idx = value.find('PM')
    # else:
    #     print('AM /  PM undefined')
    #     return -1
    ante_meridiem = value[idx:]
    if ante_meridiem == "AM":
        ante = 0
    else:
        ante = 12*60
    h_to_min = value[:idx].split(':')
    h_to_min = [int(x) for x in h_to_min]  # transfer to int

    return h_to_min[0] * 60 + h_to_min[-1] + ante


# converts b/w days and their value  - Sunday is zero and Saturday is 6
# also allows to return the value instead of key - val = "val"  -> values , value = "key" -> key
def eval_day(_day):

    # finds key
    for x in d:
        if d.get(x) == _day:
            return x
    # returns the key based on method get - value
    else:
        print("Day or value  Not Found")
        return "-1"

def new_day_of_week(total_days):
    days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    values = list(range(0, 7))
    d = dict(zip(values , days_list ))
    # check if total_days is an integer

    if not isinstance(total_days, int):
        print('Error the days input is invalid')
        return ''
    # returns the day's name

    return d[total_days % 7]


def add_time(start, duration, day=''):

    #basic calculation

    start_min = hour_to_min(start)  # returns time in minute
    dur_min = hour_to_min(duration)  # returns time in minute
    # deriving total days by div
    total_days_passed = (dur_min - start_min) // MIN_A_DAY
    # deriving the minutes at the current day
    time_without_days = (dur_min - start_min) % MIN_A_DAY


    # we put the days aside and we're left with the curren time
    hour = time_without_days // 60
    minute = time_without_days % 60

    # pick AM PM
    ante_meridiem = 'AM' if hour < 12 else 'PM'  # checks if its past noon
    hour = hour if (hour < 12) else (hour - 12)  # checks if its past noon

    _minute = '{:02d}'.format(minute)
    _hour = '{:02d}'.format(hour)


    # list of possible outcomes
    day_interval = ['', '(next day)',
                    '(' + str(total_days_passed) +
                    ' days later)']

    if day != '':
        total_days_passed = total_days_passed + eval_day(day)
    # time_str is the string returned as an answer. it's differs if the day param is specified
    if total_days_passed == 0:
        idx = 0
        time_str = (_hour + ':' + _minute + ante_meridiem + space + day_interval[idx])

    # one day options different from 2 day
    elif total_days_passed == 1:
        idx = 1
        time_str ='{}:{} {} {} {}'.format(_hour, _minute, ante_meridiem,new_day_of_week(total_days_passed),
                                         day_interval[idx])


    # 2 or more days passed
    else:
        idx = 2
        time_str = '{}:{} {} {} {}'.format(_hour, _minute, ante_meridiem, new_day_of_week(total_days_passed),
                                          day_interval[idx])

    print(time_str)

#test cases
print('Entered:  add_time("3:00 PM", "5:00",Sunday)\n')
add_time("3:00 PM", "5:00", 'Sunday')
# print()
# print('Entered:  add_time("3:00", "8:00")\n')
# add_time("3:00 AM", "8:00")
# print()
# print('Entered:  add_time("3:00", "8:00 ,Sunday)\n')
# add_time("3:00", "22:00", 'Sunday')