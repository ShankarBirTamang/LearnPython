# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution(object):
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    num_index = {}
    for i,num in enumerate(nums):
        if target-num in num_index:
            return [num_index[target-num],i]
        num_index[num]=i
    
    return []
        
nums = [2,7,11,15]
target = 9
print(twoSum("",nums,target))