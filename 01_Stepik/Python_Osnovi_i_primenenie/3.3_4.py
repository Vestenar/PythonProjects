import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r"\b(.+)\1\b", line):
        print(line)