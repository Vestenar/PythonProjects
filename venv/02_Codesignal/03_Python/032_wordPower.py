def wordPower(word):
    num = dict([(i, ord(i)-96) for i in word])
    print([(i, ord(i)-96) for i in word])
    return sum([num[ch] for ch in word])

print(wordPower("abcde"))

'''
You've heard somewhere that a word is more powerful than an action. 
You decided to put this statement at a test by assigning a power value to each action and each word. 
To begin somewhere, you defined a power of a word as the sum of powers of its characters, 
where power of a character is equal to its 1-based index in the plaintext alphabet.

Given a word, calculate its power.

Example

For word = "hello", the output should be
wordPower(word) = 52.

Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. 
Thus, the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.
'''