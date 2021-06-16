class Solution(object):

    def lexicalOrder(self, n):
        result = []
        for i in range(1, 10):
            self.dfs(result, i, n)
        return result

    # This solve the memory limit issue
    # I don't understand this though
    # why using closure consume more memory
    def dfs(self, result, i, n):
        if i <= n:
            result.append(i)

            # Adding this extra condition check
            # solve the time limit issue
            # w/o this, when you doing dfs, you need to search one more level
            # and level(k) usually has 10 times more nodes than level(k-1)
            if 10 * i > n: return

            for d in range(10):
                self.dfs(result, 10 * i + d, n)
if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]

    #deck= [17,13,11,2,3,5,7]
    n=13
    res = Solution().lexicalOrder(n)


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key = str)

