class Solution:
    def moveZeroes(self, nums) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1





# 时间复杂度：O(n)O
#
# 但是，操作是最优的。代码执行的总操作（数组写入）是非 0 元素的数量.
#
# 空间复杂度：O(1)，
#
# 只使用了常量空间。

if __name__ == "__main__":
    nums = [1,2,0,1,0,1]
    res = Solution().moveZeroes(nums)
    print(res)