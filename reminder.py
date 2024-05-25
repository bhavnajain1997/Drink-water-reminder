import time
from win10toast import ToastNotifier 
import datetime

hours = int(input("Hours of interval: "))
minutes = int(input("Minutes of interval: "))
seconds = int(input("seconds of interval: "))
time_interval = seconds + (minutes * 60) + (hours * 3600)
print(time_interval)
currenttime = datetime.datetime.now()
print(currenttime.strftime("%H : %M : %S" ) )

def getmessage():
    notification = ToastNotifier()
    notification.show_toast("Time to drink water now")
    
if __name__ == '__main__':
    while True :
        time.sleep(time_interval)
        getmessage()




