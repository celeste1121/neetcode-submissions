# Hash map: key is num, value is frequency
# [1:1,2:2,3:3]
# sorted by values
# pop the largest k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        
        for num in nums:
            res[num] += 1
        
        sorted_res = sorted(res, key = res.get, reverse=True)
        
        return sorted_res[:k]
# time: O(m*nlogn)
# space: O(m*n)
