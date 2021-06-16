#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/84-by-ikaruga/
"""
需要看上面解释单调栈特点
"""
#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: #特殊情况
            return 0
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j+1] += 1
                else:
                    heights[j+1] = 0
                #遍历每一行更新最大面积
                for j in range(col+2):
                    while stack and heights[stack[-1]] > heights[j]:
                        temp = stack.pop()
                        width = j - stack[-1] - 1
                        height = heights[temp]
                        res = max(res, width*height)
                    stack.append(j)
        return res

