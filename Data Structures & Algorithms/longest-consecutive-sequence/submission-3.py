# find the samllest as starting point
# check if num - 1 not in the nums
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # search in set is O(1)
        longestSeq = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longestSeq = max(longestSeq, length)
        return longestSeq
# Time complexity: O(n)
# Space: O(n)