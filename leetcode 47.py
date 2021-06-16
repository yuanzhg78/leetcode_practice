class Solution:
    def permuteUnique(self, nums):
        nums.sort() #the purpose of sort: put the same number together
        res = []
        visited = set()
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(nums)):#注意i在这里是index 所以存的时候是index不是数值
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):#这句话为了skip the same number 已经finish dfs of the first branch
                #！！！！若某一个元素和上一个元素相等, 并且上一个元素没有被使用过，说明它俩在同一层;
                # 若某一个元素和上一个元素相等, 并且上一个元素被使用过，说明这个元素在上一个元素的子树中
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res
if __name__ == '__main__':
    nums = [1,1,2]

    solution = Solution()
    result = solution.permuteUnique(nums)
    print(result)


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()#升序排列
        res = []

        self.dfs(candidates, size, 0, [], target, res)
        return res

    def dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])#path是引用传值，如果不用copy，那么p最终的结果是[]
            return

        for index in range(start, size):
            if candidates[index] > residue:
                break

            if index > start and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])
            self.dfs(candidates, size, index + 1, path, residue - candidates[index], res)
            path.pop()#当输出结果之后，会回溯到上一步，之后将path中的元素pop出，寻找下一组组合。










