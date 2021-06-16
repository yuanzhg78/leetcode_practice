class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            l = start
            r = end - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if not nums and k == 0:
            return
        length = len(nums)
        k = k % length

        reverse(nums, 0, length - k)
        reverse(nums, length - k, length)
        reverse(nums, 0, length)

