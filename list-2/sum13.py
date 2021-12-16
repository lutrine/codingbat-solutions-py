"""Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count."""


def sum13(nums):
    # if nums is an empty array, return 0
    if nums == []:
        return 0

    # variables
    length = len(nums)
    total = 0

    # if the first value doesn't equal 13, add it
    if nums[0] != 13:
        total += nums[0]  # adds first value
    # start from 1 because we already added the first value
    # end at "length" because we need to check if the last value is 13 or not
    for i in range(1, length):
        # if the current value and value before don't equal 13, add the current value
        if nums[i] != 13 and nums[i - 1] != 13:
            total += nums[i]  # adds curent value
    return total
