#二分法
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1 #位运算
            counter = 0
            for num in nums:
                if num <= mid:
                    counter += 1
            if counter > mid:
                right = mid
            else:
                # ！！！！难点
                left = mid + 1

        return left


# 【注意】如果小于等于 mid 的个数如果多于 mid，例如：
            # 8 个萝卜 放在 7 个坑里，就至少有 1 个坑里至少有 2 个萝卜
            # 这个坑的位置可能是 1、2、3、4、5、6、7
            # 重复的数就一定在 [1, mid] 里面，包括 1 和 mid
            # 此时，不排除中位数的分支逻辑好想，因此写在前面

#https://www.zhihu.com/question/36132386  知乎二分法
#快慢指针


class Solution(object):
    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]  # next
            fast = nums[nums[fast]]  # next.next
            if slow == fast:
                break

        fast = nums[0]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]

        return slow

#
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         low = 0
#         high = len(nums)-1
#         while low < high:
#             mid = (low + high) // 2
#             count = 0
#             for i in nums:
#                 if i <= mid:
#                     count += 1
#             if count <= mid:
#                 low = mid + 1
#             else:
#                 high = mid
#         return low