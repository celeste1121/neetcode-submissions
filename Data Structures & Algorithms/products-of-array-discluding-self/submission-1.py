# we can't use division cause num can be 0
# we should use prefix and suffix
# example 1: prefix list, suffix list
# [1,1,2,8], [48,24,6,1]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
# Time: O(n)
# Space: O(n)
