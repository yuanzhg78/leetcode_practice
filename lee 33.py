class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 判断target值是在[左边界, 中值]区间还是[右边界, 中值]区间
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            # print(left, right, mid)
            if nums[mid] == target:
                return mid
            judge1 = nums[left] < nums[mid] and target < nums[mid] and target >= nums[left]  # 左半边有序
            judge2 = nums[left] > nums[mid] and (target < nums[mid] or target >= nums[left])  # 左半边旋转

            if judge1 or judge2:  # target在左半边
                right = mid - 1
                mid = (left + right) // 2
            else:  # target在右半边
                left = mid + 1
                mid = (left + right) // 2

        return -1



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        # while循环中有等于判断
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
