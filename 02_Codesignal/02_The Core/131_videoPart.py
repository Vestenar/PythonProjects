from math import gcd
def videoPart(part, total):
    p = convert(part)
    t = convert(total)
    g = gcd(t,p)
    return [p//g, t//g]

def convert(t):
    con = zip([int(i) for i in t.split(":")], [2,1,0])
    return sum(i*(60**j) for i,j in con)

part = "02:20:00"
total = "07:00:00"
print(videoPart(part, total))
part = "01:41:59"
total = "02:00:00"
print(videoPart(part, total))

'''
You have been watching a video for some time. 
Knowing the total video duration find out what portion of the video you have already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
videoPart(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.
'''
