import datetime
def newYearCelebrations(takeOffTime, minutes):
    hh,mm = (int(i) for i in takeOffTime.split(":"))
    if hh == 00 and mm == 00:
        ny = datetime.datetime(2001,1,1,hh,mm)
        count = 1
    else:
        ny = datetime.datetime(2000,12,31,hh,mm)
        count = 0
    for i in range(len(minutes)-1,0,-1):
        temp = minutes[i-1]
        minutes[i] -= temp
    print(minutes)
    if ny.year == 2000: yearback = True
    else: yearback = False
    for i in minutes:
        ny += datetime.timedelta(minutes=i)
        if (ny.year == 2001 and yearback) or (ny.year == 2001 and ny.minute== 0 and ny.hour==0):
            count +=1
            yearback = False
        ny -= datetime.timedelta(hours=1)
        if (ny.year == 2001 and ny.minute== 0 and ny.hour==0):
            count += 1
        if ny.year == 2000:
            yearback = True

    return count if ny.year == 2001 else count+1


# takeOffTime = "23:35"
# minutes = [60, 90, 140]
takeOffTime = "00:00"
minutes = [60, 120, 180, 250]
print(newYearCelebrations(takeOffTime,minutes), "== 4")
'''
You're a pretty busy billionaire, and you often fly your personal Private Jet to remote places. 
Usually travel doesn't bother you, but this time you are unlucky: 
it's New Year's Eve, and since you have to fly halfway around the world, 
you'll probably have to celebrate New Year's Day in mid-air!

Your course lies west of your current location and crosses several time zones. 
The pilot told you the exact schedule: it is known that you will take off at takeOffTime, 
and in minutes[i] after takeoff you will cross the ith border between time zones. 
After crossing each border you will have to set your wrist watch one hour earlier 
(every second matters to you, so you can't let your watch show incorrect time). 
It is guaranteed that you won't cross the IDL 
(i.e. after crossing each time zone border your current time will be set one hour back).

You've been thinking about this situation and realized that it might be 
a good opportunity to celebrate New Year's Day more than once, 
i.e. each time your wrist watch shows 00:00. 
Assuming that you set your watch immediately after the border is crossed, 
how many times will you be able to celebrate this New Year's Day with a nice bottle of champagne? 
Note that the answer should include celebrations both in mid-air and on the ground 
(it doesn't matter if the plane landed in the last time zone before the midnight or not, 
you'll not let the last opportunity to celebrate New Year slip through your fingers).

Example

For takeOffTime = "23:35" and minutes = [60, 90, 140],
the output should be
newYearCelebrations(takeOffTime, minutes) = 3.

Here is the list of events by the time zones:

    initial time zone:
        at 23:35 your flight starts;
        at 00:00 you celebrate New Year for the first time;
        at 00:35 (60 minutes after the take off) you cross the first border;
    time zone -1:
        at 23:35 you cross the border (00:35 by your initial time zone);
        at 00:00 you celebrate New Year for the second time (01:00 by your initial time zone);
        at 00:05 (90 minutes after the take off) you cross the second border;
    time zone -2:
        at 23:05 you cross the border;
        at 23:55 (140 minutes after the take off) you cross another border;
    time zone -3:
        at 22:55 you cross the border;
        at 00:00 you celebrate New Year for the third time.

Thus, the output should be 3. That's a lot of champagne!
'''
