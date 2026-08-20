# Python DATETIME & TIME MODULE

from datetime import datetime , timedelta , timezone
import time

# current data & time
'''
def current_datetime():

    now = datetime.now()

    print("Current Date & Time : " , now)
    
current_datetime()


def current_datetime():

    now = datetime.now()

    print("Year : " , now.year)
    print("Month : " , now.month)
    print("Day : " , now.day)
    print("Hour : " , now.hour)
    print("minute : " , now.minute)
    print("second : " , now.second)

current_datetime()


# Current Time in Seconds

def time_seconds():

    seconds = time.time()

    print("Second since 1 jan 1970 : " , seconds)

time_seconds()

# Date & Time formatting

def format_datetime():

    now = datetime.now()

    print("DD-MM-YYYY : " , now.strftime("%d-%m-%Y"))
    print("YYYY/MM/DD : " , now.strftime("%Y/%m/%d"))
    print("12 - Hours : " , now.strftime("%I : %M : %S %p"))
    print("24 - Hours : " , now.strftime("%H:%M:%S"))

format_datetime()


# Number of Days Between two Dates

def date_diffrence():

    start_data = input("Enter start date (YYYY-MM-DD) : ")
    end_data = input("Enter end date (YYYY-MM-DD) : ")

    date1 = datetime.strptime(start_data , "%Y-%m-%d")
    date2 = datetime.strptime(end_data , "%Y-%m-%d")

    days = abs(date2 - date1)

    print("Total Days : " , days)

date_diffrence()


def date_diffrence():
    
    today = datetime.now()

    future_time = today - timedelta(days = 10)

    print("Today : " , today.strftime("%d-%m-%Y"))
    print("diffrence ; " , future_time.strftime("%d-%m-%Y"))

date_diffrence()
'''
# UTC and LOCAL time

def utc_local_time():
    utc_time = datetime.now(timezone.utc)
    local_time = datetime.now()

    print(utc_time)
    print(local_time)
utc_local_time()

    
