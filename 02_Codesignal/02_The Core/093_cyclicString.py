def cyclicString(s):
    for i in range(1,len(s)+1):
        cycle = s[:i]*(len(s)//len(s[:i])+1)
        print(cycle)
        if s in cycle:
            return i



s = "bcaba"
print(cyclicString(s))


'''
You're given a substring s of some cyclic string. 
What's the length of the smallest possible string that can be concatenated to itself 
many times to obtain this cyclic string?

Example

For s = "cabca", the output should be
cyclicString(s) = 3.

"cabca" is a substring of a cycle string "abcabcabcabc..." 
that can be obtained by concatenating "abc" to itself. Thus, the answer is 3.
'''
