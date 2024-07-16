import datetime
import time

def showTime():
    print("Hello wolrd from Azure functions!")
    print("Current date and time in Norway: ")
    now = datetime.datetime.now()
    # Print the current date and time in a specific format
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
  showTime()
