import requests
from math import log

file = requests.get("https://projecteuler.net/project/resources/p099_base_exp.txt")

current_string = 0
base1, pow1, lg1, str_max = 1, 0, 0, 0

for i in file.iter_lines():
    base2, pow2 = map(int, str(i)[2:-1].split(","))
    lg2 = pow2*log(base2)
    current_string += 1
    if lg2 > lg1:
        base1, pow1, lg1 = base2, pow2, lg2
        str_max = current_string

print("String with max number: {}".format(str_max))
