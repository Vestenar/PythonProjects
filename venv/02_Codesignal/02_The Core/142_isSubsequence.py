import re
def isSubsequence(t, s):
    pattern = ''
    for ch in s:
        # pattern += "["+ch+"].*"
        pattern += ch + '.*' if ch not in ['.','?','!','=','*','+','-'] else "\\"+ch+'.*'
    print(pattern)
    return re.search(pattern, t) is not None


t = "he sd.f dsk e8.sd??l**23, 23,f.s++83+"
s = "h  8.?*3+"
print(isSubsequence(t, s))
'''
Given a string s, determine if it is a subsequence of a given string t.

Example

    For t = "CodeSignal" and s = "CoSi", the output should be
    isSubsequence(t, s) = true;

    For t = "CodeSignal" and s = "cosi", the output should be
    the output should be
    isSubsequence(t, s) = false.

'''
