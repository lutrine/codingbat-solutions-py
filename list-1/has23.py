"""Given an int array length 2, return True if it contains a 2 or a 3."""


def has23(nums):
    for i in range(len(nums)):
        if nums[i] == 2 or nums[i] == 3:
            return True
    return False
