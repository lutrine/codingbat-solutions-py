"""Given an array of ints, return the number of 9's in the array."""


def array_count9(nums):
    nines = 0  # placeholder
    for i in range(len(nums)):  # checks each number
        # add to counter if index of nums equals 9
        if nums[i] == 9:
            nines = nines + 1
    return nines
