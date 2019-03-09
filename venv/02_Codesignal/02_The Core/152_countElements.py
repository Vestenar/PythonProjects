import ast


def countElements(inputString):
    inputString = inputString.replace("true", "True")
    inputString = inputString.replace("false", "False")
    ans = ast.literal_eval(inputString)
    if type(ans) != list:
        return 1
    else:
        inputString = inputString.replace("[", "")
        inputString = "[" + inputString.replace("]","") +"]"
        return len(ast.literal_eval(inputString))


inputString = "[[0, 20], [33, 99]]"
print(countElements(inputString))
inputString = "[ \"one\", 2, \"three\" ]"
print(countElements(inputString))
inputString = "true"
print(countElements(inputString))
inputString = "[[1, 2, [3]], 4]"
print(countElements(inputString))
inputString = "[\"oh, no! kind, of, tricky\", \"test, case\"]"
print(countElements(inputString))
# inputString = "\"try this!, [1, 2, 3, 32], False\""
# print(countElements(inputString))
# inputString = "\"a,,,,,,,,,,,,,,asdf\""
# print(countElements(inputString))
# inputString = "1023456789"
# print(countElements(inputString))
'''
You've been invited to a job interview at a famous company that tests programming challenges. 
To evaluate your coding skills, they have asked you to parse a given problem's input given as an inputString string, 
and count the number of primitive type elements within it.

The inputString can be either a primitive type variable or an array (possibly multidimensional) 
that contains elements of the primitive types.
A primitive type variable can be:

    an integer number;
    a string, which is surrounded by " characters (note that it may contain any character except ");
    a boolean, which is either true or false.

Return the total number of primitive type elements inside inputString.

Example

    For inputString = "[[0, 20], [33, 99]]", the output should be
    countElements(inputString) = 4;
    For inputString = "[ "one", 2, "three" ]", the output should be
    countElements(inputString) = 3;
    For inputString = "true", the output should be
    countElements(inputString) = 1;
    For inputString = "[[1, 2, [3]], 4]", the output should be
    countElements(inputString) = 4.

'''
