class Solution:
    #回溯 dfs
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

#回溯的过程是执行一次深度优先遍历，一条路走到底，走不通的时候，返回回来，继续执行，一直这样下去，直到回到起点。
from typing import List
class Solution:
    def subsets(self, nums) :
        size = len(nums)
        if size == 0:
            return []
        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()#删除刚加入的元素

if __name__ == "__main__":
    nums=[1,2,3]
    res = Solution().subsets(nums)
    print(res)


    class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            if not nums: return [[]]
            res = []
            for p in self.subsets(nums[1:]):
                res.append(p)  # 把子集加上
                # print(nums[:1]+p)
                res.append(nums[:1] + p)
            return res




