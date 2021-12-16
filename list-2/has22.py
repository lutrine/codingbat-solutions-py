"""Given an array of ints, return True if the array contains a 2 next to a 2 
somewhere."""


def has22(nums):
    for i in range(1, len(nums), 1):
        # checks the number behind so that the last number in the array can be
        # checked as well
        if nums[i - 1] == 2 and nums[i] == 2:
            return True
    return False
