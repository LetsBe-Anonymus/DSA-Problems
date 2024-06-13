class Solution:
    def minimumChairs(self, s: str) -> int:
        curCount, maxCount = 0,0
        for c in s:
            if c == "E":
                curCount += 1
                maxCount = max(maxCount, curCount)
            else:
                curCount -= 1
        return maxCount