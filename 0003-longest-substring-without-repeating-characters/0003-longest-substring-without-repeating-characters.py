class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueElements = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in uniqueElements:
                uniqueElements.remove(s[l])
                l += 1
            uniqueElements.add(s[r])
            res = max(res, (r - l) + 1)
        return res
