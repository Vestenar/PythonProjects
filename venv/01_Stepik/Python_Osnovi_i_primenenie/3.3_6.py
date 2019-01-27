import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b[a]+\b", "argh", line, count=1, flags=re.IGNORECASE))


'''
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
'''