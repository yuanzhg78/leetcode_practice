class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=-1
        n=len(nums)
        def reversenum(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                k=i
                break
        if k==-1:
            reversenum(nums,0,n-1)
            return
        l=-1
        for i in range(n-1,k,-1):
            if nums[i] > nums[k]:
                l=i
                break
        nums[k],nums[l]=nums[l],nums[k]

        reversenum(nums, k + 1, n - 1)


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().nextPermutation(nums))




