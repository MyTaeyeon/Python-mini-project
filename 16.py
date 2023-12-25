import plyer, time

while True:
    plyer.notification.notify(title='ALERT', message='Take a break!', timeout=10)
    time.sleep(10)