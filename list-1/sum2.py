"""Given an array of ints, return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements that exist, 
returning 0 if the array is length 0."""


def sum2(nums):
    # if the list is length 0, return 0
    if len(nums) == 0:
        return 0
    # if the list is length 1, return index 0
    elif len(nums) == 1:
        return nums[0]
    # return the sum of the first 2 elements
    else:
        return nums[0] + nums[1]
