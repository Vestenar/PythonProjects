import re
import time

start_time = time.time()


def lrc2subRip(lrcLyrics, songLength):
    subrip = []
    for i in range(0, len(lrcLyrics) - 1):
        subrip.append(str(i + 1))
        ss1 = lrcLyrics[i][4:9].replace('.', ',') + '0'
        ss2 = lrcLyrics[i + 1][4:9].replace('.', ',') + '0'
        mm1 = int(lrcLyrics[i][1:3]) % 60
        mm2 = int(lrcLyrics[i + 1][1:3]) % 60
        hh1 = int(lrcLyrics[i][1:3]) // 60
        hh2 = int(lrcLyrics[i + 1][1:3]) // 60
        t_start = "{:02}:{:02}:{}".format(hh1, mm1, ss1)
        t_end = "{:02}:{:02}:{}".format(hh2, mm2, ss2)
        subrip.append(t_start + " --> " + t_end)
        subrip.append(lrcLyrics[i][10:].strip())
        subrip.append("")
    else:
        subrip.append(str(i + 2))
        ss1 = lrcLyrics[i + 1][4:9].replace('.', ',') + '0'
        mm1 = int(lrcLyrics[i + 1][1:3]) % 60
        hh1 = int(lrcLyrics[i + 1][1:3]) // 60
        t_start = "{:02}:{:02}:{}".format(hh1, mm1, ss1)
        t_end = songLength + ',000'
        subrip.append(t_start + " --> " + t_end)
        subrip.append(lrcLyrics[i + 1][10:].strip())
    return subrip


#  еще одно красивое решение
def lrc2subRip0(lrcLyrics, songLength):
    r, count = [], 1
    time = [[int(s[i:i + 2]) for i in [1, 4]] + [s[7:9]] for s in lrcLyrics]
    time = ['{:02d}:{:02d}:{:02d},{}'.format(x // 60, x % 60, y, z.ljust(3, '0')) for x, y, z in time] + [
        songLength + ',000']
    for index, s in enumerate(lrcLyrics):
        r.extend([str(count), time[index] + ' --> ' + time[index + 1], s[11:], ''])
        count += 1
    return r[:-1]


#  решение с регуляркой
def lrc2subRip2(lrcLyrics, songLength):
    pattern = r"\[(\d{2}):(\d{2})\.(\d{2})\](?: (.*))?"
    regex = re.compile(pattern)

    times = []
    lyrics = []
    for line in lrcLyrics:
        m, s, ms, lyric = regex.match(line).groups()
        times.append("{:02}:{:02}:{:02},{:02}0".format(int(m) // 60, int(m) % 60, int(s), int(ms)))
        lyrics.append(lyric)

    times.append(songLength + ",000")

    result = []
    for i in range(len(lrcLyrics)):
        result.append(str(i + 1))
        result.append("{} --> {}".format(times[i], times[i + 1]))
        result.append(lyrics[i] or "")
        result.append("")

    return result[:-1]


#  решение с функцией конвертирования времени
def lrc2subRip3(lrcLyrics, songLength):
    def timeConvert(time):
        mm, ss, xx = map(int, re.split(r":|\.", time))
        hh = mm / 60
        mm %= 60
        return "%02d:%02d:%02d,%03d" % (hh, mm, ss, xx * 10)

    ans = []
    for k, line in enumerate(lrcLyrics):
        t = timeConvert(line[1:9])
        if ans: ans[-3] += " --> " + t
        ans.extend([str(k + 1), t, line[11:], ""])
    if ans: ans[-3] += " --> " + songLength + ",000"
    return ans[:-1]


lrcLyrics = ["[00:09.01]",
             "[00:10.01] Sweet dreams are made of this",
             "[00:13.26] Who am I to disagree?",
             "[00:17.01] Travel the world and the seven seas",
             "[00:20.95] Everybodys looking for something",
             "[00:24.57]",
             "[00:24.82] Some of them want to use you",
             "[00:28.64] Some of them want to get used by you",
             "[00:32.45] Some of them want to abuse you",
             "[00:36.32] Some of them want to be abused",
             "[00:40.32]",
             "[00:52.00] Sweet dreams are made of this",
             "[00:55.37] Who am I to disagree?",
             "[00:59.18] Travel the world and the seven seas",
             "[01:03.00] Everybodys looking for something",
             "[01:48.34] Some of them want to use you",
             "[01:52.16] Some of them want to get used by you",
             "[01:55.97] Some of them want to abuse you",
             "[01:59.72] Some of them want to be abused",
             "[02:03.58]",
             "[01:18.17]",
             "[01:29.17] Hold your head up, movin on",
             "[01:19.18] Hold your head up",
             "[01:31.11] Keep your head up",
             "[01:19.92] Keep your head up, movin on",
             "[01:21.86] Hold your head up, movin on",
             "[01:23.74] Keep your head up, movin on",
             "[01:25.67] Hold your head up, movin on",
             "[01:27.55] Keep your head up, movin on"]

songLength = "02:23:44"
print(lrc2subRip(lrcLyrics, songLength))
print("--- %s seconds ---" % (time.time() - start_time))
'''
During your most recent trip to Codelandia you decided to buy a brand new CodePlayer, 
a music player that (allegedly) can work with any possible media format. 
As it turns out, this isn't true: the player can't read lyrics written in the LRC format. 
It can, however, read the SubRip format, so now you want to translate all the lyrics you have
from LRC to SubRip.

Since you are a pro programmer (no noob would ever get to Codelandia!), 
you're happy to implement a function that, given lrcLyrics and songLength, 
returns the lyrics in SubRip format.

Example

For

lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
             "[00:17.20] Happy birthday to you!"]

and songLength = "00:00:20", the output should be

lrc2subRip(lrcLyrics, songLength) = [
  "1",
  "00:00:12,000 --> 00:00:17,200",
  "Happy birthday dear coder,",
  "",
  "2",
  "00:00:17,200 --> 00:00:20,000",
  "Happy birthday to you!"
]

'''
