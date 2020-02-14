# import datetime
#
# def regularMonths(currMonth):
#     mm, yy = map(int, currMonth.split("-"))
#     while True:
#         if mm < 12:
#             mm += 1
#         else:
#             mm = 1
#             yy +=1
#         m = datetime.date(yy, mm, 1)
#         if m.weekday() == 0:
#             return m.strftime("%m-%Y")


from datetime import datetime  # импортирует класс datetime.datetime!


def regularMonths(currMonth):
    d = datetime.strptime(currMonth, '%m-%Y')
    m = d.month
    y = d.year

    while True:
        if m % 12 == 0:
            y += 1
        m = (m % 12) + 1
        d = datetime(y, m, 1)
        print(d)
        if d.weekday() == 0:
            # Today is a Monday.
            return datetime.strftime(d, '%m-%Y')

currMonth = "2-2016"
print(regularMonths(currMonth))


'''
In an effort to be more innovative, your boss introduced a strange new tradition: 
the first day of every month you're allowed to work from home. 
You like this rule when the day falls on a Monday, because any excuse to skip rush hour traffic is great!

You and your colleagues have started calling these months regular months. 
Since you're a fan of working from home, you decide to find out how far away the nearest regular month is, 
given that the currMonth has just started.

For your convenience, here is a list of month lengths (from January to December, respectively):

    Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

Please, note that in leap years February has 29 days.

Example

For currMonth = "02-2016", the output should be
regularMonths(currMonth) = "08-2016".

February of 2016 year is regular, but it doesn't count since it has started already, 
so the next regular month is August of 2016 - which is the answer.

'''
