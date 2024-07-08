import datetime
import time

while(True):
    print("Hello wolrd from Azure!")
    print("Current date and time: ")
    now = datetime.datetime.now()
    # Print the current date and time in a specific format
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)
