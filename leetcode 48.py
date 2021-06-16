s=0
e=len(matrix)-1
while s<=e:
    t1=s
    t2=e
    while t1 != e:
        temp=matrix[s][t1]
        matrix[s][t1]=matrix[t2][s]
        matrix[t2][s]=matrix[e][t2]
        matrix[e][t2]=matrix[t1][e]
        matrix[t1][e]=temp
    s+=1
    e+=1





class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        begin = 0
        end = len(matrix)-1
        while begin <= end:
            tem1 = begin
            tem2 = end
            while tem1 != end:
                temp = matrix[begin][tem1]
                matrix[begin][tem1] = matrix[tem2][begin]
                matrix[tem2][begin] = matrix[end][tem2]
                matrix[end][tem2] = matrix[tem1][end]
                matrix[tem1][end] = temp
                tem1 = tem1+1
                tem2 = tem2-1
            begin = begin+1
            end = end-1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
