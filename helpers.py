import calendar
import datetime

def format_time(time) -> str:
    # Convert to str with AM, PM units
    new_time = ''
    if len(time) == 0:
        return new_time # Skip rest of code below, terminate early

    # Specific time given by user
    hour = int(time[:2])
    if hour >= 1 and hour < 10:
        new_time = time[1:] + ' AM' # remove leading 0
    elif hour == 10 or hour == 11:
        new_time = time + ' AM'
    elif hour == 12:
        new_time = time + ' PM'
    elif hour == 0:
        # convert 0 o clock to 12 o clock
        new_time = '12' + time[2:] + ' AM'
    else:
        # convert to regular 12 hour time
        result = hour - 12
        if result < 10:
            new_time = str(result)
        else:
            new_time = '1' + str(result - 10)
        new_time += time[2:] + ' PM'
    return new_time



def format_date(task_appt_date) -> str:
    date_obj = None
    if task_appt_date:
        # Appt date is given as YYYY-MM-DD format
        month_index = int(task_appt_date[5:7]) # int
        month = calendar.month_name[month_index] # str
        day = task_appt_date[8:] # str
        year = task_appt_date[0:4] # str
        date_obj = datetime.date(int(year), month_index, int(day)) # date object
        day_of_week = calendar.day_name[date_obj.weekday()]
        task_appt_date = day_of_week + ", " + month + " " + day + ", " + year
    else: # account for optional appt dates
        task_appt_date = None
    return task_appt_date
