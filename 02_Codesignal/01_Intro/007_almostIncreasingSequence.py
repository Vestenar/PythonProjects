def almostIncreasingSequence(sequence):
    data = True
    count = 0
    for i in range(len(sequence)):
        if count > 2:
            data = False
            break
        if i+1 < len(sequence) and sequence[i] >= sequence[i+1]:
            count += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]:
            count += 1

    return data

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert almostIncreasingSequence([1, 3, 2, 1]) == False, "First"
    assert almostIncreasingSequence([1, 3, 2]) == True, "Second"
    assert almostIncreasingSequence([1, 2, 1, 2]) == False, "Third"
    assert almostIncreasingSequence([1, 4, 10, 4, 2]) == False, "Fourth"
    assert almostIncreasingSequence([10, 1, 2, 3, 4, 5]) == True, "Fifth"
    assert almostIncreasingSequence([1, 1, 1, 2, 3]) == False, "Sixth"
    assert almostIncreasingSequence([0, -2, 5, 6]) == True, "Seventh"
    assert almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]) == False, "Eighth"
    assert almostIncreasingSequence([40, 50, 60, 10, 20, 30]) == False, "Nineth"
    assert almostIncreasingSequence([1, 1]) == True, "Tenth"
    assert almostIncreasingSequence([1, 2, 5, 3, 5]) == True, "Eleventh"
    assert almostIncreasingSequence([1, 2, 5, 5, 5]) == False, "Twelveth"
    assert almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]) == False, "Thirteenth"
    assert almostIncreasingSequence([1, 2, 3, 4, 3, 6]) == True, "Fourteenth"
    assert almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]) == True, "Fifteenth"
    assert almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]) == True, "Sixteenth"
    assert almostIncreasingSequence([3, 5, 67, 98, 3]) == True, "Seventeenth"
    print('You are awesome! All tests are done! Go Check it!')

'''
Given a sequence of integers as an array, determine whether 
it is possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.

Example

    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. 
    Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
'''