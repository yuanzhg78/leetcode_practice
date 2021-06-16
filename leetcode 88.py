class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m+n]=nums2[:n] #先合并再排序
        nums1.sort()
class Solution:#下方是解释
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        for k in range(m+n-1,-1,-1):
            if i==-1:
                nums1[k]=nums2[j]
                j-=1
            elif j==-1:
                break
            elif nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1


#https://leetcode-cn.com/problems/merge-sorted-array/solution/si-xiang-mei-you-chuang-xin-de-di-fang-zhu-yao-ti-/
#归并排序 从前到后 #首选
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        # 从后向前归并，比较 nums1 和 nums2 末尾的元素哪个大，谁大谁出列，覆盖 nums1
        for k in range(m + n - 1, -1, -1):
            # 注意：同样要把 nums1 和 nums2 归并完成的逻辑写在前面，否则会出现数组下标越界异常
            if i == -1:
                # 这里直接把 nuns2 还没看的元素复制到 nums1 即可
                # 我们可以在循环中完成
                nums1[k] = nums2[j]
                j -= 1
            elif j == -1:
                # 注意：这里直接 break 掉就可以了
                # 因为 nums2 遍历完成以后，nums1 剩下的元素虽然还没有看，但一定是排定以后的那个样子
                break
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1



#时间复杂度：O(M + N)    这里 M 是数组 nums1 的长度，N 是数组 nums2 的长度。
#空间复杂度：O(1)，该算法没有使用额外的存储空间，仅使用了常数个临时变量用于比较。

