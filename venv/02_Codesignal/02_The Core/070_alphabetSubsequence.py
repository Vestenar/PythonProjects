def alphabetSubsequence(s):
    prev = 0
    for i in s:
        if ord(i)>prev:
            prev = ord(i)
        else: return False
    return True

print(alphabetSubsequence("afe"))


def alphabetSubsequence2(s):
    return all(s[i]<s[i+1] for i in range(len(s)-1))  # all -> True если все значения истинны

print(alphabetSubsequence2("afe"))
'''
Check whether the given string is a subsequence of the plaintext alphabet.

Example

    For s = "effg" or s = "cdce", the output should be
    alphabetSubsequence(s) = false;
    For s = "ace" or s = "bxz", the output should be
    alphabetSubsequence(s) = true.

'''