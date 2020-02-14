import datetime

date = input().split()
yy,mm,dd = (int(c) for c in date)
d = datetime.date(yy,mm,dd)+datetime.timedelta(days=int(input()))
print(d.year, d.month, d.day)

