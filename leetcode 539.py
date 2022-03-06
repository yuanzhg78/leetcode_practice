class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []
       for time in timePoints:
            hh, mm = map(int, time.split(':'))
            nums.append(hh * 60 + mm)

        nums.sort()

        n = len(nums)
        res = 1440
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            res = min(res, d)
        res = min(res, nums[0] + 1440 - nums[-1])

        return res



但是要注意最后一个和第一个时间差值

