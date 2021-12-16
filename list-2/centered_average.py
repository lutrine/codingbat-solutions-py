"""Return the "centered" average of an array of ints, which we'll say is the 
mean average of the values, except ignoring the largest and smallest values in 
the array. If there are multiple copies of the smallest value, ignore just one 
copy, and likewise for the largest value. Use int division to produce the final 
average. You may assume that the array is length 3 or more."""


def centered_average(nums):
    total = 0
    # get maximum & minimum
    maximum = max(nums)
    minimum = min(nums)
    # add each number in the list to variable "total"
    for i in range(len(nums)):
        total += nums[i]
    # subtract the maximum and minimum from the total
    total -= maximum + minimum
    # return the total divided by the length of the list without max and min
    return total // (len(nums) - 2)
