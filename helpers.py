def get_seconds_to_alarm(alarm_str):
    from datetime import datetime

    # Getting hour & min
    alarm_hr, alarm_mt = alarm_str.split(':')

    now = datetime.now()
    alarm = datetime.now()

    alarm = alarm.replace(hour=int(alarm_hr), minute=int(alarm_mt), second=0)

    now_timestamp = now.timestamp()
    alarm_timestamp = alarm.timestamp()

    # If alarm was passed, calculate alarm for next day
    seconds_to_next_alarm = (alarm_timestamp - now_timestamp)
    if seconds_to_next_alarm < 0:
        seconds_to_next_alarm += 24 * 60 * 60  # Adding 1 day: 24 hours x 60 minutes/hr x 60 seconds/min

    return seconds_to_next_alarm
