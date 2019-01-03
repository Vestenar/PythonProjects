def fileNaming(names):
    newname = []

    for name in names:
        if name in newname:
            k = 1
            while name + '(' + str(k) + ')' in newname:
                k += 1
            name += '(' + str(k) + ')'
        newname.append(name)
    return newname


assert fileNaming(["doc",
 "doc",
 "image",
 "doc(1)",
 "doc"]) == ["doc",
         "doc(1)",
         "image",
         "doc(1)(1)",
         "doc(2)"], "1"

assert fileNaming(["a(1)",
 "a(6)",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a"]) == ["a(1)",
         "a(6)",
         "a",
         "a(2)",
         "a(3)",
         "a(4)",
         "a(5)",
         "a(7)",
         "a(8)",
         "a(9)",
         "a(10)",
         "a(11)"], "2"

assert fileNaming(["dd",
 "dd(1)",
 "dd(2)",
 "dd",
 "dd(1)",
 "dd(1)(2)",
 "dd(1)(1)",
 "dd",
 "dd(1)"]) == ["dd",
             "dd(1)",
             "dd(2)",
             "dd(3)",
             "dd(1)(1)",
             "dd(1)(2)",
             "dd(1)(1)(1)",
             "dd(4)",
             "dd(1)(3)"], "3"
print("well done")


'''
You are given an array of desired filenames in the order of their creation. 
Since two files cannot have equal names, the one which comes later will have an addition 
to its name in a form of (k), where k is the smallest positive integer such 
that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].'''