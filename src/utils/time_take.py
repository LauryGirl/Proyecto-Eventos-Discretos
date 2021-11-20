def get_time(t):
    th = t / 60
    str_min = str(th - int(th))
    str_min = str_min[2:4] if len(str_min) > 3 else str_min[2:]
    percent_min = int(str_min)
    minutes = int(percent_min * 60 / 100)

    hour = (10 + int(th)) % 12
    if hour == 0:
        hour = 12
    
    return str(hour) + ':' + str(minutes) if minutes > 9 else str(hour) + ':0' + str(minutes)