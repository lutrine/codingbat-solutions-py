"""Given an array of ints length 3, figure out which is larger, the first or 
last element in the array, and set all the other elements to be that value. 
Return the changed array."""


def max_end3(nums):
    largest = 0
    # if first > last then first = largest
    if nums[0] > nums[len(nums) - 1]:
        largest = nums[0]
    # else last = largest
    else:
        largest = nums[len(nums) - 1]

    # replace each number with largest
    for i in range(len(nums)):
        nums[i] = largest
    return nums
