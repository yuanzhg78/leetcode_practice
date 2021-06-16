class Solution:
    #利用矩阵的第一行和第一列保存该行或者列是否应被置为0  O(MN) O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag_row=False #判断第一行是否需要置0
        flag_col=False #判断第一列是否需要置0
        m=len(matrix) #行
        n=len(matrix[0])#列
        for i in range(m):  #遍历第一列，若第一列中存在0
            if(matrix[i][0]==0):
                flag_col=True #置0列的flag
                break
        for i in range(n):
            if(matrix[0][i]==0): #遍历第一行，若第一行中存在0，将flag_row=True,表示需要将第一行置0
                flag_row=True
                break
        for i in range(1,m):
            for j in range(1,n):  #遍历矩阵，遍历区间，行区间[1,m)，列区间[1,n)，若matrix[i][j]==0，则将对应的行和列记录下来，
                # 即将第一行和第一列中对应的位置置为0。matrix[i][0]=matrix[0][j]=0
                if(matrix[i][j]==0):
                    matrix[i][0]=matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][0]==0 or matrix[0][j]==0):#再遍历一次矩阵，若当前位置的行或列索引对应的第一行或者第一列处为0，
                    # 即matrix[i][0]==0 or matrix[0][j]==0，将此位置置为0。
                    matrix[i][j]=0
        if(flag_col):
            for i in range(m):
                matrix[i][0]=0
        if(flag_row):
            for i in range(n):
                matrix[0][i]=0
