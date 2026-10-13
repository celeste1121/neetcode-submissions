# fix the first number, and then find the sec in the rest of list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        secondN = 0
        for i in range(len(nums) - 1):
            secondN = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == secondN:
                    return [i, j]
# time: O(n square)
# space: O(1)