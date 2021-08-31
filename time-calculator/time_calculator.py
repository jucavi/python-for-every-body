def parse_time(time):
    halve = ""
    hours, rest = time.split(":")
    
    if rest.endswith('M'):
        minutes, halve = rest.split()
    else:
        minutes = rest
        
    return int(hours), int(minutes), halve


def result_day(week_day, days_later):
    DAYS_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = DAYS_OF_THE_WEEK.index(week_day.capitalize())
    index = (days_later - 7 + day) % 7
    return DAYS_OF_THE_WEEK[index]

def time_sum(start, duration):
    start_h, start_m, halve = parse_time(start)
    duration_h, duration_m, _ = parse_time(duration)
    
    if halve == "PM":
        start_h = start_h + 12
    
    minutes = start_m + duration_m   
    hour, minutes = divmod(minutes, 60)
    total_hours = start_h + duration_h + hour
    days, hours = divmod(total_hours, 24)
    
    return days, hours, minutes, halve

def message(hours, minutes, halve, days_later, week_day):
    base = f'{str(hours)}:{str(minutes):0>2} {halve}'
    
    if days_later == 0:
        if not week_day: 
            return base
        else:
            return base + f", {week_day}"
        
    if days_later == 1:
        if not week_day: 
            return base + " (next day)"
        else:
            return base + f", {week_day} (next day)"
        
    if not week_day: 
        return base + f" ({days_later} days later)"
    else:
        return base + f", {week_day} ({days_later} days later)"
        
        
def add_time(start, duration, week_day=""):
    days_later, hours, minutes, halve = time_sum(start, duration)
    
    if week_day:
        week_day = result_day(week_day, days_later)
    
    if hours < 12:
        halve = 'AM'
    elif hours == 12:
        halve = 'PM'
    else:
        hours -= 12
        halve = 'PM'
        
    if hours == 0:
        hours = 12
    
    output = message(hours, minutes, halve, days_later, week_day)
    return output