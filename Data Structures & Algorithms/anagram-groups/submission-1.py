# instintct: using sorted
# template
# res = defaultdict(list)

# for s in strs:
#     key = ...
#     res[key].append(s)

# return list(res.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creates a dictionary where each key automatically gets an empty list when accessed for the first time
        res = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word)) # sorted becomes list, and list can't be dictionary key, so we turn this into string
            res[key].append(word)
        return list(res.values())

# time: O(m * nlongn)
# space: O(m*n)
