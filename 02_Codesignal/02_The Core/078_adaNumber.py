def adaNumber(line):

    try:
        int(line)
        return True
    except:
        if line[0] == "#" or line[-1] != "#" or line.count("#") != 2:
            return False
        else:
            line = line.replace("_", "")
            num = line.split("#")
            try:
                base = int(num[0])
                if 2 > base or base > 16:
                    return False
                int(num[1], base)
                return True
            except:
                return False





line = "1_4#___C63A_4ecc6_5B362d__3#"
print(line, adaNumber(line))
line = "123_13"
print(line, adaNumber(line))
line = "17#ac#"
print(line, adaNumber(line))
line = "123_456_789"
print(line, adaNumber(line))
line = "16#123abc#"
print(line, adaNumber(line))
line = "10#10#123ABC#"
print(line, adaNumber(line))
line = "10##"
print(line, adaNumber(line))

'''
Consider two following representations of a non-negative integer:

    A simple decimal integer, constructed of a non-empty sequence of digits from 0 to 9;
    An integer with at least one digit in a base from 2 to 16 (inclusive), 
enclosed between # characters, and preceded by the base, which can only be a 
number between 2 and 16 in the first representation. 
For digits from 10 to 15 characters a, b, ..., f and A, B, ..., F are used.

Additionally, both representations may contain underscore (_) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.

Your task is to determine whether the given string is a valid integer representation.

Note: this is how integer numbers are represented in the programming language Ada.

Example

    For line = "123_456_789", the output should be
    adaNumber(line) = true;
    For line = "16#123abc#", the output should be
    adaNumber(line) = true;
    For line = "10#123abc#", the output should be
    adaNumber(line) = false;
    For line = "10#10#123ABC#", the output should be
    adaNumber(line) = false;
    For line = "10#0#", the output should be
    adaNumber(line) = true;
    For line = "10##", the output should be
    adaNumber(line) = false.

'''
