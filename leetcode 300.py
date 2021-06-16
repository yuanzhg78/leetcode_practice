# # 动态规划
#dp[i] 以i为结尾（一定包括i）所能形成的最长上升子序列
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#         return 0
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
#向前遍历找到比i小的元素j元素，然后进行计算



#动态规划+二分查找
# Dynamic programming + Dichotomy.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        res = 0
        for num in nums:
            left = 0
            right = res
            while left < right:
                mid = left + (right - left) // 2  # 防止溢出
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            if right == res:
                res += 1
        return res

if __name__ == "__main__":
    nums=[10,9,2,5,3,7]
    res = Solution().lengthOfLIS(nums)
    print(res)
#https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/






