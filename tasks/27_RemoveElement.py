"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.



"""
import pytest


nums = [0, 1, 2, 2, 3]
val = 2
out = []
k = 0


def remove_element(nums, val, k):
    for i in range(len(nums)):
        if nums[i] == val:
           out.insert(len(out), "_")
           k += 1
        else:
            out.insert(0, nums[i])
    return out, k


def add_3(x):
    return x + 3


print(remove_element(nums, val, k))


def test_answer():
    assert remove_element([0, 1, 2, 2, 3], 2, 0) == ([3, 1, 0, '_', '_'], 2)
def test_add():
    assert add_3(3) == 6

