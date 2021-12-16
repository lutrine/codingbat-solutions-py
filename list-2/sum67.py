"""Return the sum of the numbers in the array, except ignore sections of 
numbers starting with a 6 and extending to the next 7 (every 6 will be followed 
by at least one 7). Return 0 for no numbers."""


def sum67(nums):
    count = True
    total = 0
    for i in range(0, len(nums), 1):
        if nums[i] == 6:
            count = False
        elif nums[i] != 6 and count == True:
            total += nums[i]
        elif nums[i] == 7:
            count = True
    return total
