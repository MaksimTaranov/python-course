class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        minn = -2**31-1
        max1, max2, max3 = minn, minn, minn
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2 and n != max1:
                max3 = max2
                max2 = n
            elif n > max3 and n != max2 and n != max1:
                max3 = n
        if max3 == minn:
            return max1
        else:
            return max3
