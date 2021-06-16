class Solution:
    def addDigits(self, num: int) -> int:
        if num < 9:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num%9


class Solution:#求和的方式做
    def missingNumber(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = len(nums)
        return int((1 / 2) * n * (n + 1) - sum(nums))
