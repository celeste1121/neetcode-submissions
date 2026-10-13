# hash map key as characters, index as number
# compare the hash map of s and t to see are they the same
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        countS, countT = {}, {}
        # Initilize the index as 0 when the character not in the hash map
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],1) +1
            countT[t[i]] = countT.get(t[i],1) +1
        
        return countS == countT

# Time: O(n) where n = len(s) = len(t)
# Space: O(1): hash map for limited characters is 1