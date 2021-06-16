#https://leetcode-cn.com/problems/spiral-matrix/solution/pythondan-ceng-xun-huan-jian-dan-yi-dong-by-gao-si/
#右下左上
class Solution:
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 : return []
        lenX = len(matrix[0])
        lenY = len(matrix)
        startX = 0
        endX = lenX
        startY = 0
        endY = lenY
        l = []
        while (startX <= endX and startY <= endY):
            if (startY<endY):
                for i in range(startX,endX):
                    l.append(matrix[startY][i])
            startY+=1
            if (startX<endX):
                for i in range(startY,endY):
                    l.append(matrix[i][endX-1])
            endX-=1
            if (startY<endY):
                for i in range(startX,endX)[::-1]:
                    l.append(matrix[endY-1][i])
            endY-=1
            if (startX<endX):
                for i in range(startY,endY)[::-1]:
                    l.append(matrix[i][startX])
            startX+=1
        return l
class Solution: #leetcode 59
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while c<=n*n:
            # 从左向右
            for i in range(j, n-j):
                array[j][i] = c
                c += 1
            # 从上往下走
            for i in range(j+1, n-j):
                array[i][n-j-1] = c
                c += 1
            # 从右往左走
            for i in range(n-j-2, j-1, -1):
                array[n-j-1][i] = c
                c += 1
            # 从下往上走
            for i in range(n-j-2, j, -1):
                array[i][j] = c
                c += 1
            j += 1
        return array
