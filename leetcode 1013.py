# 先整体求和，不能被 3 整除直接返回 False。
# 再用双指针，分别计算两边的和是否满足等于 sum/3。
# 注意：题目的意思就是相邻元素相加，而不是任意相加。

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        amount = sum(arr)
        left = 0
        right = len(arr) - 1
        l_sum, r_sum = arr[left],arr[right]
        while left + 1 < right:
            if l_sum == r_sum == amount/3:
                return True
            if l_sum != amount/3:
                left += 1
                l_sum += arr[left]
            if r_sum != amount/3:
                right -= 1
                r_sum += arr[right]
        return False
