# build-in function
def largestNumber1(self, nums):
    if not any(nums):
        return "0"
    return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))

class Solution(object):
# bubble sort
    def largestNumber2(self, nums):
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #print(int("".join(map(str, nums))))
        return str(int("".join(map(str, nums))))


    def compare(self, n1, n2):
        print(str(n1)+str(n2))
        return str(n1) + str(n2) > str(n2) + str(n1)


if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]

    nums= [3,30,34,5,9]
    res=Solution().largestNumber2(nums)


# quick sort, in-place
def largestNumber(self, nums):
    self.quickSort(nums, 0, len(nums) - 1)
    return str(int("".join(map(str, nums))))


def quickSort(self, nums, l, r):
    if l >= r:
        return

    pos = self.partition(nums, l, r)
    self.quickSort(nums, l, pos - 1)
    self.quickSort(nums, pos + 1, r)


def partition(self, nums, l, r):
    low = l
    while l < r:
        if self.compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

def compare(self, n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

