class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(numRows):
            temp=[1]*(i+1)
            res.append(temp)
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res



if __name__ == '__main__':
    numRows=5

    solution = Solution()
    result = solution.generate(numRows)
    print(result)