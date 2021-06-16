class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            start = matrix[i][0]
            end = matrix[i][-1]
            if end < target:
                continue
            elif start > target:
                break
            else:
                print(matrix[i])
                if target in matrix[i]:

                    return True
        return False



if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]

    matrix= [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

    #pre = createTree(pre)
    #post=createTree(post)
    res=Solution().searchMatrix(matrix,5)

class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n==0:return False
        m = len(matrix[0])
        if m==0:return False
        index = m-1
        for i in range(n):
            while index>=0 and matrix[i][index]>target:
                index-=1
            if index == -1:break
            if matrix[i][index]==target:return True
        return False