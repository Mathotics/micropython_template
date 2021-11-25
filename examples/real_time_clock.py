# Example using the real-time clock

from machine import RTC # Required for using the real-time clock

rtc = RTC() # Get an Instance of the real-time clock
rtc.datetime((2021, 8, 23, 2, 12, 48, 0, 0)) # set a specific date and
                                             # time, eg. 2017/8/23 1:12:48

for _ in range(100):
    print(rtc.datetime()) # get date and time and print it out
    time.sleep(1) # Put the thread to sleep for 1 second