#############################################################################
# Course: codePost 101
# Student: student1@codepost.io
# Assignment: Loops
#
#############################################################################

def find_max(some_array):
    """
    Return the maximum element of some_array (int array).
    """

    # keep track of the maximum element observed in the array
    maxSoFar = 0

    for i in range(0, len(some_array)):
        if (some_array[i] > maxSoFar):
            maxSoFar = some_array[i]

    return maxSoFar

def reverse(some_array):
    """
    Reverse the positions of the elements of some_array (int array).
    """
    for i in range(0, len(some_array) // 2 + 1):
        swapIndex = len(some_array)-1-i

        temp = some_array[swapIndex]

        # perform swap
        some_array[swapIndex] = some_array[i]
        some_array[i] = temp

    return some_array


def shift_by_one(some_array):
    """
    Move element i in some_array to position i+1. Move
    the last element  to position 0.
    """

    if len(some_array) > 1:
        lastValue = some_array[0]

        for i in range(0, len(some_array)):
            if i == len(some_array) - 1:
                some_array[0] = lastValue
            else:
                temp = some_array[i+1]
                some_array[i+1] = lastValue
                lastValue = temp

    return some_array