import re
def swapAdjacentWords(s):
    print(s)
    return re.sub(r"(\w+) (\w+)", r"\2 \1", s)



s = "How are you today guys"
print(swapAdjacentWords(s))


'''
You are given a string consisting of words separated by whitespace characters, 
where the words consist only of English letters. Your task is to swap pairs of 
consecutive words and return the result.

Example

    For s = "CodeFight On", the output should be
    swapAdjacentWords(s) = "On CodeFight";
    For s = "How are you today guys", the output should be
    swapAdjacentWords(s) = "are How today you guys".


'''