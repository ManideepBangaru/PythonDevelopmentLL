from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():
    # today = date.today()
    # print("Today's date is : ",today)
    # print("Date Components : ",today.day,today.month,today.year)
    # print("Today's weekday Number : ",today.weekday())
    # days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    # print("Which is a ",days[today.weekday()])

    # today = datetime.now()
    # print("Today's date is : ",today)
    # print(today.day,today.month,today.year)
    # print(today.weekday())
    # print(today.isoweekday())
    #
    # # Get the current time
    # t = datetime.time(datetime.now())
    # t1 = datetime.time(today)
    # print(t)
    # print(t1)

    # now = datetime.now()
    # print(now.strftime("Current Year is : %Y"))
    # print(now.strftime("%a, %d, %B, %y"))
    # print(now.strftime("%B %d,%Y"))
    #
    # print(now.strftime("locale time is : %c"))
    # print(now.strftime("locale time is : %x"))
    # print(now.strftime("locale time is : %X"))

    # print(timedelta(days=365, hours=5, minutes=1))
    # now = datetime.now()
    # print("today is : ",str(now))
    # print("one year from now will be : ", now + timedelta(days=365))

    # c = calendar.TextCalendar(calendar.MONDAY)
    # st = c.formatmonth(2017,1,0,0)
    # print(st)

    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2017,1)
    print(st)



if __name__ == "__main__":
    main()