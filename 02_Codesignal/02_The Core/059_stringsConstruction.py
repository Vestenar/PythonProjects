def stringsConstruction(a, b):
    # ans = []
    # for i in a:
    #     ans.append(b.count(i)//a.count(i))
    return min(b.count(i)//a.count(i) for i in a)


a = "hnccv"
b = "hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"
print(stringsConstruction(a,b))
a = "zzz"
b = "zzzzzzzzzzz"
print(stringsConstruction(a,b))
'''
How many strings equal to a can be constructed using letters from the string b? 
Each letter can be used only once and in one string only.

Example

For a = "abc" and b = "abccba", the output should be
stringsConstruction(a, b) = 2.

We can construct 2 strings a with letters from b.
'''
