#game of life 生命游戏
#用2bit 位运算
#https://blog.csdn.net/qq_17550379/article/details/83959020
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 8个方向的邻居
        for i in range(row):
            for j in range(col):
                lives = 0
                for m, n in neighbors:  # 这样遍历可以提出元组里的元素
                    if 0 <= i + m < row and 0 <= j + n < col:
                        lives += board[i + m][j + n] & 1
                if board[i][j] == 1 and 2 <= lives < 4:
                    board[i][j] = 3

                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1  # 将数组中的3和2换成0和1的形式，位移即可



# 我们这里使用2bit表示状态变化（current to next）。我们先遍历board，看每个节点周围有多少个初始状态是live，
# 如果这个节点原先是live并且周围的2<=lives<4，我们知道它现在的状态应该是live->live，也就是对应上面的编码3。
# 如果这个节点原先是die并且周围是lives==3，我们知道它现在的状态应该是die->live，也就是对应上面的编码2。
# 这些都做完之后，我们在此遍历board，将其中的2和3调整回来（live or die），
