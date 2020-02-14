import re
def longestWord(text):
    # for char in text:
    #     if char in "?,.!/;:[]{}()-\\":
    #         text = text.replace(char, '')
    # n = text.split()
    n = re.split('[^a-zA-Z]+', text)
    print(n)
    max = n[0]
    for word in n:
        if len(word) > len(max):
            max = word
    return max


task = "You are the best!!!!!!!!!!!! CodeFighter ever___________"
print(longestWord(task))

result = re.findall(r'@[a-zA-Z]+.\w+',
                    'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".'''
