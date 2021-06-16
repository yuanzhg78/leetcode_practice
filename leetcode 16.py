class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort
        n=len(nums)
        ans=float("inf")
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end = n-1
            while start<end:
                s=nums[i]+nums[start]+nums[end]
                if s== target:
                    return target
                if abs(ans-target)>abs(s-target):
                    ans=s
                if s<target:
                    start+=1
                elif s>target:
                    end-=1
        return ans

        nums.sort()
        # print(nums)
        n = len(nums)
        res = float("inf")  # Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                # print(left,right)
                cur = nums[i] + nums[left] + nums[right]
                if cur == target: return target
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
        return res