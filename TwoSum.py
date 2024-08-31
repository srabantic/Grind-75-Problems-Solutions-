"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
# Solution with O(n^2) Time Complexity


def twoSum(self, nums: List[int], target: int) -> List[int]:
    result_value = 0
    result_list = []
    for i in range(0, len(nums)):
        result = nums[i]
        for j in range(i+1, len(nums)):
            result = nums[i] + nums[j]
            if (result == target):
                result_list.append(i)
                result_list.append(j)
                return result_list

# Solution with O(n) Time Complexity


def twoSum(self, nums: List[int], target: int) -> List[int]:
    value_seen = {}
    for i in range(0, len(nums)):
        value_diff = target - nums[i]
        if (value_diff in value_seen):
            return [value_seen[value_diff], i]
        else:
            value_seen[nums[i]] = i
