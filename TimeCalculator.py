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
    idx = value.find('M')
    if idx != -1:
        ante_meridiem = value[idx - 1:]
        if (ante_meridiem == "AM"):
            ante=0
        else:
            ante = 12 * 60
    else:
        ante = 0
        idx = len(value)

    h_to_min = value[:idx-1].split(':')
    h_to_min = [int(x) for x in h_to_min]  # transfer to int

    return h_to_min[0] * 60 + h_to_min[-1] + ante


# converts b/w days and their value  - Sunday is zero and Saturday is 6
# also allows to return the value instead of key - val = "val"  -> values , value = "key" -> key
def eval_day(_day):
    for x in d:        # finds key
        if d.get(x) == _day:
            return x
    # returns the key based on method get - value
    else:
        print("Day or value  Not Found")
        return "-1"

def new_day_of_week(presentedDays):
    # check if presentedDays is an integer

    if not isinstance(presentedDays, int):
        print('Error the days input is invalid')
        return ''
    # returns the day's name
    return d[presentedDays % 7]

def add_time(start, duration, day=''):

    #basic calculation
    start_min = hour_to_min(start)  # returns time in minute
    dur_min = hour_to_min(duration)  # returns time in minute
    # deriving total days by div
    absoluteDays = (start_min + dur_min) // MIN_A_DAY
    # deriving the minutes at the current day
    time_without_days = (start_min + dur_min) % MIN_A_DAY

    # we put the days aside and we're left with the curren time
    hour = time_without_days // 60
    minute = time_without_days % 60 #last calculation

    time_str = calc_to_output(day, absoluteDays, hour, minute)
    print(time_str)


def calc_to_output(day, absoluteDays, hour, minute):  # arranges data output
    # Start of design the output
    ante_meridiem = 'AM' if hour < 12 else 'PM'  # checks if its past noon
    hour = hour if (hour < 12) else (hour - 12)  # checks if its past noon
    _minute = '{:02d}'.format(minute)
    _hour = '{:02d}'.format(hour)
    # list of possible outcomes

    # assert  absoluteDays == 1,f"number 1, got: {eval_day(day) + absoluteDays}"
    # assert eval_day(day) == 3 ,f"number 1, got: {eval_day(day)}"


    #invokes print_time to get  string output form
    time_s = print_time(_hour, _minute, ante_meridiem, day, absoluteDays)
    return time_s

def print_time(_hour, _minute, ante_meridiem, day, absoluteDays): #arranges the output into a string
    presentedDays = absoluteDays + eval_day(day)
    if day != '':      #case day is filled
        day_interval = [day, new_day_of_week(presentedDays) + '(next day)',
                        new_day_of_week(presentedDays) + '(' + str(absoluteDays) +
                        ' days later)']
    else: #case day is empty
        day_interval = ['', '', '']
    # time_str is the string returned as an answer. it's differs if the day param is specified
    if absoluteDays == 0:
        j = 0
        time_str = '{}:{} {} {}'.format(_hour, _minute, ante_meridiem, day_interval[j])
    # one day options different from 2 day
    elif absoluteDays == 1: #writes next day
        j = 1
        time_str = '{}:{} {} {}'.format(_hour, _minute, ante_meridiem, day_interval[j])
    # 2 or more days passed
    else: #reports n days later
        j = 2
        time_str = '{}:{} {} {} '.format(_hour, _minute, ante_meridiem, day_interval[j])

    return time_str




#test cases
#print('Entered:  add_time("3:00 PM", "10:00",Sunday)\n')
add_time("4:00 PM", "4:00", "Tuesday")


print('\nPredicted: (8:00 PM, Tuesday\n')
# print()
# print('Entered:  add_time("3:00", "8:00")\n')
# add_time("3:00 AM", "8:00")
# print()
# print('Entered:  add_time("3:00", "8:00 ,Sunday)\n')
# add_time("3:00", "22:00", 'Sunday')