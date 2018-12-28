def evenDigitsOnly(n):
    for i in str(n):
        if int(i)%2 != 0:
            return False
    return True

'''
Check if all digits of the given integer are even.

Example

    For n = 248622, the output should be
    evenDigitsOnly(n) = true;
    For n = 642386, the output should be
    evenDigitsOnly(n) = false.
'''