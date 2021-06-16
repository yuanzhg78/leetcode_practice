class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = list()
        if not matrix:
            return result
        r, c = len(matrix), len(matrix[0])
        x1, y1, x2, y2 = 0, 0, c - 1, r - 1
        while x1 <= x2 and y1 <= y2:
            for i in range(x1, x2 + 1):
                result.append(matrix[y1][i])

            for j in range(y1 + 1, y2 + 1):
                result.append(matrix[j][x2])
            if x1 < x2 and y1 < y2:
                for i in range(x2 - 1, x1, -1):
                    result.append(matrix[y2][i])

                for j in range(y2, y1, -1):
                    result.append(matrix[j][x1])

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1

        return result


if __name__ == "__main__":
    matrix = [[6, 9, 7]]
    print(Solution().spiralOrder(matrix))


class Solution(object):
    # 递归解法，从外向里一圈一圈地按顺序扫描
    def spiralOrder(self, matrix):
        ans = []
        # 矩阵为空直接返回
        if (len(matrix) == 0):
            return ans
        self.func(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, ans)
        return ans

    # 用来将外围一圈的数字按顺序放到数组里面
    # ri,rj,ci,cj用来限定矩阵的边界
    def func(self, matrix, ri, rj, ci, cj, nums):
        # 如果矩阵空直接返回
        if (ri > rj or ci > cj):
            return
        # 如果矩阵是横着一条或者竖着一条，按顺序扫描后返回
        elif (ri == rj):
            for j in range(ci, cj + 1):
                nums.append(matrix[ri][j])
            return
        elif (ci == cj):
            for i in range(ri, rj + 1):
                nums.append(matrix[i][ci])
            return
        # 矩阵的长宽至少为2时，扫描外围，对除掉外围后的矩阵递归调用
        else:
            for j in range(ci, cj):
                nums.append(matrix[ri][j])
            for i in range(ri, rj):
                nums.append(matrix[i][cj])
            for j in range(cj, ci, -1):
                nums.append(matrix[rj][j])
            for i in range(rj, ri, -1):
                nums.append(matrix[i][ci])
            self.func(matrix, ri + 1, rj - 1, ci + 1, cj - 1, nums)



class Solution:
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 :
            return []
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

