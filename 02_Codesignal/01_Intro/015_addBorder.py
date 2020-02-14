def addBorder(picture):
    picture.insert(0,"*" * len(picture[0]))
    picture.append("*" * len(picture[0]))
    for i in range(len(picture)):
        test = picture[i]
        test = "*" + test + "*"
        picture[i] = test
    return picture

'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''