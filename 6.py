import datetime

current_date = datetime.datetime.now().date()

timeAlarm = input('Enter the time of alarm to be set: HH:MM:SS\n')
timeAlarm = datetime.datetime.strptime(f'{current_date} {timeAlarm}', '%Y-%m-%d %H:%M:%S')

while True:
    now = datetime.datetime.now()
    
    if now >= timeAlarm:
        print("Time's up!")