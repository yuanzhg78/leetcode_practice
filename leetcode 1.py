class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashdict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashdict and i != hashdict[complement]:
                return [i, hashdict[complement]]
            hashdict[num] = i


if __name__ == "__main__":
    nums=[2,7,11,15]
    print(Solution().twoSum(nums,9))