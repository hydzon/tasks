"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.



"""

nums = [0, 1, 2, 2, 3, 0, 4, 2, 3, 8, 9, 2, 2, 2, 2]
val = 2
out = []
k = 0

for i in range(len(nums)):
    if nums[i] == val:
       out.insert(len(out), "_")
       k += 1
    else:
        out.insert(0, nums[i])

print(k, out)
