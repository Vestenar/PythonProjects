def validTime(time):
    hm = time.split(':')
    return 0 <= int(hm[0]) <=23 and 0<= int(hm[1]) <= 59


# используя метод map
# def validTime(time):
#     h,m=map(int,time.split(":"))
#     return 0<=h<24 and 0<=m<60



task = "13:58"
print(validTime(task))
'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

    For time = "13:58", the output should be
    validTime(time) = true;
    For time = "25:51", the output should be
    validTime(time) = false;
    For time = "02:76", the output should be
    validTime(time) = false.
'''