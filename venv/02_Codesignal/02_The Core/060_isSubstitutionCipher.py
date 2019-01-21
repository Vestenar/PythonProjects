def isSubstitutionCipher(s1, s2):
    ans1, ans2 = "", ""
    dic1, dic2 = dict(zip(s1,s2)), dict(zip(s2,s1))
    for i in range(len(s1)):
        ans1+=dic1[s1[i]]
        ans2+=dic2[s2[i]]
    return ans1 == s2 and ans2 ==s1

string1 = "aacb"
string2 = "aabc"


string1 = "aaxyaa"
string2 = "aazzaa"
print(isSubstitutionCipher(string1,string2))

string1 = "dccd"
string2 = "zzxx"

'''
A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging 
some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext 
alphabet is replaced with the corresponding (i.e. having the same index) letter of some 
ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other 
using some (possibly, different) substitution ciphers.

Example

    For string1 = "aacb" and string2 = "aabc", the output should be
    isSubstitutionCipher(string1, string2) = true.

    Any ciphertext alphabet that starts with acb... would make this transformation possible.

    For string1 = "aa" and string2 = "bc", the output should be
    isSubstitutionCipher(string1, string2) = false.

'''
