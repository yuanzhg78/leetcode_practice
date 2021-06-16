from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, ans = defaultdict(int), list()
        for i in nums1: dic[i] += 1
        for i in nums2:
            if dic[i] != 0:
                ans.append(i)
                dic[i] -= 1
        return ans

#建立一个哈希表，键为nums1的数，值为这个数出现的次数
#遍历num2,当num2的数出现在哈希表中，将它添加到答案里，同时更新哈希表，让其出现次数减一。

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums = set(nums1) & set(nums2)
        res = []
        for i in nums:
            res += [i] * min(nums1.count(i), nums2.count(i))
        return res