def variableName(name):
    if not name[0].isalpha() and name[0] != '_':
        return False
    else:
        for i in range(1, len(name)):
            if not name[i].isalnum() and name[i] != '_':
                return False

    return True


'''Correct variable names consist only of English letters, digits and underscores 
and they can't start with a digit.

Check if the given string is a correct variable name.

Example

    For name = "var_1__Int", the output should be
    variableName(name) = true;
    For name = "qq-q", the output should be
    variableName(name) = false;
    For name = "2w2", the output should be
    variableName(name) = false.

'''