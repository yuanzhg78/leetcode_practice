class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first= second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                 return True
        return False


# Start with the maximum numbers for the first and second element. Then:
# (1) Find the first smallest number in the 3 subsequence
# (2) Find the second one greater than the first element, reset the first one if it's smaller