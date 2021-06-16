class Solution:
    def findKthLargest1(self, nums, k: int) -> int:
        def partition(left, right): #快排
            # if left>= right:
            #     return
            pivot = nums[left]
            l=left
            h=right
            while l<h:
                while l<h and nums[h]<=pivot:
                    h-=1
                nums[l]=nums[h]
                while l<h and nums[l] > pivot:
                    l+=1
                nums[h]=nums[l]
            nums[l]=pivot
            print(nums)
            return h

        left = 0
        right = len(nums) - 1

        while 1:
            idx = partition(left, right)

            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1


if __name__ == "__main__":

    nums = [4, 3, 6, 5, 2]
    res = Solution().findKthLargest1(nums, 2)
    # res = Solution().findKthLargest(nums,2)
    print(res)


class Solution(object):
    def findKthLargest(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            p = self.partition(nums, left, right)

            if p == k - 1:
                return nums[p]
            elif p < k - 1:
                left = p + 1
            else:
                right = p - 1

    def partition(self, nums, left, right):
        # k=random.randint(left,right)
        k = left
        pivot = nums[k]
        index = left
        for i in range(left + 1, right + 1):
            if nums[i] >= pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        print(nums)
        return index


if __name__ == "__main__":
    nums = [4,3,6,5,2]
    #res = Solution().findKthLargest(nums, 2)
    print(res)

