#首选
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        k=1
        for i in range(n):
            res[i]=k
            k=k*nums[i]
        k=1
        for i in range(n-1,-1,-1):
            res[i]*=k
            k*=nums[i]
        return res

#O(N)
#O(N) 借助了res一个存结果
#https://leetcode-cn.com/problems/product-of-array-except-self/solution/bao-cun-zuo-ji-he-you-ji-python3-by-zhu_shi_fu/



class Solution(object):
    def productExceptSelf(self, nums):
        """
        利用两个数组，一个是数nums[i]左边的所有数字的乘积（不包括 nums[i]）
        一个是nums[i]右边的所有数字的乘积
        然后利用上面的两个数组，对应位置相乘就可以得到除了 nums[i] 本身以外其他的乘积了
        如果想达到空间复杂度O(1)那么可以直接用输出的数组，取代 上面的两个数组，保存中间计算结果
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [];
        right = [];
        mul = 1
        output = []
        for num in nums:
            left.append(mul)
            mul *= num
        mul = 1
        for num in nums[::-1]:
            right.append(mul)
            mul *= num
        right = right[::-1]
        for l, r in itertools.izip(left, right):
            output.append(l*r)
        return output