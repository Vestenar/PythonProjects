import datetime


def curiousClock(someTime, leavingTime):
    yyyy, mm, dd, h, m = (int(i) for i in someTime.split()[0].split("-")+someTime.split()[1].split(":"))
    s = datetime.datetime(yyyy, mm, dd, h, m)
    yyyy, mm, dd, h, m = (int(i) for i in leavingTime.split()[0].split("-") + leavingTime.split()[1].split(":"))
    l = datetime.datetime(yyyy, mm, dd, h, m)
    s -= l - s
    out = "{}-{:02d}-{:02d} {:02d}:{:02d}".format(s.year, s.month, s.day, s.hour, s.minute)
    n = s.strftime("%Y-%m-%d %H:%M")
    print(n)
    return out

someTime = "2016-08-26 22:40"
leavingTime = "2016-08-29 10:00"
print(curiousClock(someTime, leavingTime))


'''
Benjamin recently bought a digital clock at a magic trick shop. 
The seller never told Ben what was so special about it, but mentioned that 
one day Benjamin would be faced with a surprise.

Indeed, the clock did surprise Benjamin: without warning, at someTime 
the clock suddenly started going in the opposite direction! Unfortunately, 
Benjamin has an important meeting very soon, and knows that at leavingTime 
he should leave the house so as to not be late. Ben spent all his money on the clock, 
so has to figure out what time his clock will show when it's time to leave.

Given the someTime at which the clock started to go backwards, 
find out what time will be shown on the curious clock at leavingTime.

For your convenience, here is the list of months lengths (from January to December, respectively):

    Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

Please, note that in leap years February has 29 days.

Example

For someTime = "2016-08-26 22:40" and leavingTime = "2016-08-29 10:00", the output should be
curiousClock(someTime, leavingTime) = "2016-08-24 11:20".

There are 2 days, 11 hours and 20 minutes till the meeting. 
Thus, the clock will show 2016-08-24 11:20 at the leavingTime.
'''
