import csv

d = {}
with open(r'c:\adb\Crimes.csv') as listing:
    # names = []
    crimes = csv.DictReader(listing)
    # print(list(crimes))
    for crime in crimes:
        print(crime,end="\n\n")
        if crime["Primary Type"] not in d:
            d[crime["Primary Type"]] = 0
        else: d[crime["Primary Type"]] +=1
    a = {k:v for v,k in d.items()}
    print(a[max(a.keys())])
    print(a)


