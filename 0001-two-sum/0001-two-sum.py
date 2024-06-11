class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNum = {}

        for i,n in enumerate(nums):
            reqSum = target-n
            if reqSum in previousNum:
                return [previousNum[reqSum], i]
            previousNum[n] = i