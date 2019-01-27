import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r"z...z", line):
        print(line)