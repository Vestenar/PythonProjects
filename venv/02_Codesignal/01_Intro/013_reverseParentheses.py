def reverseParentheses(s):
    while ')' in s:
        j = s.index(')')
        i = s.rindex('(', 0, j)
        s = s[:i] + s[j-1:i:-1] + s[j+1:]
    return s

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert reverseParentheses("a(bc)de") == "acbde", "First"
    assert reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq", "Second"
    assert reverseParentheses("co(de(fight)s)") == "cosfighted", "Third"
    assert reverseParentheses("Code(Cha(lle)nge)") == "CodeegnlleahC", "Fourth"
    assert reverseParentheses("Where are the parentheses?") == "Where are the parentheses?", "Fifth"
    assert reverseParentheses("abc(cba)ab(bac)c") == "abcabcabcabc", "Sixth"
    assert reverseParentheses("The ((quick (brown) (fox) jumps over the lazy) dog)") == "The god quick nworb xof jumps over the lazy", "Seventh"
    print('You are awesome! All tests are done! Go Check it!')


'''
You have a string s that consists of English letters, 
punctuation marks, whitespace characters, and brackets. 
It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, 
starting from the innermost pair. The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".'''