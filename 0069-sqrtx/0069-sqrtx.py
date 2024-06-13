class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        left = 1 
        right = x

        while left <= right:
            # mid = left + (right-left) // 2
            mid = (left+right)//2
            pot = mid*mid
            if pot == x:
                return mid
            elif pot > x:
                right = mid - 1
            elif pot < x:
                left = mid + 1

        return right


