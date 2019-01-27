import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if not re.findall(" ", line):
        if len(re.findall(r"\b(0|1(01*0)*1)*\b", line)[0][0]) != 0: # stackowerflow
            print(line)