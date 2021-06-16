class Solution(object):#hashmap
    def majorityElement(self, nums):
        dict = {}
        Max = nums[0]
        for i in nums:
            if dict.get(i):
                dict[i] = dict[i] + 1
                if dict[i] > dict[Max]:
                    Max = i
            else:
                dict[i] = 1
        return Max

class Solution(object):#众数的数量大于 n/2n/2,排完序后中间的数就是众数
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)/2]

