class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_list = [str(x) for x in range(1, 10)]

        def isValid(list1, list2):
            for x in list1:
                if x == '.':
                    continue
                if x in list2:
                    return False
                elif x in valid_list:
                    list2.append(x)
                else:
                    return False
            return True

        def isValidRow(board): #判断每一行是否有问题
            for list1 in board:
                temp_list = []
                if not isValid(list1, temp_list):
                    return False
            return True

        def isValidColumn(board): #判断每一列是否有问题
            for i in range(9):
                column_list = []
                temp_list = []
                for j in range(9):
                    column_list.append(board[j][i])
                if not isValid(column_list, temp_list):
                    return False
            return True

        def isValid33(board):#判断每个3乘3方格有没有问题
            for i in range(3):
                for j in range(3):
                    three_list = []
                    temp_list = []
                    for x in range(3):
                        for y in range(3):
                            three_list.append(board[i * 3 + x][j * 3 + y])
                    if not isValid(three_list, temp_list):
                        return False
            return True

        return isValidRow(board) and isValidColumn(board) and isValid33(board)


import collections
#https://segmentfault.com/a/1190000010081065

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 哈希表的键为：行、列、宫；值为每行的元素、每列的元素、每个宫的元素
        hash_map = collections.defaultdict(list)
        # 对每个格子遍历一遍，先遍历行
        for i, row in enumerate(board):
            # 再遍历列
            for j, elem in enumerate(row):
                # 如果该格子的元素不为空，则需要进行判断
                if elem != '.':
                    # 该格子的所处行在哈希表中的名字
                    row_key = 'row' + str(i)
                    # 该格子的所处列在哈希表中的名字
                    col_key = 'col' + str(j)
                    # 该格子所处的宫在哈希表中的名字
                    sector_key = 'sec' + str(i // 3) + str(j // 3)
                    # 如果该各自的值在行/列/宫中已存在，则说明该数独无效。
                    if elem in hash_map[row_key] or elem in hash_map[col_key] or elem in hash_map[sector_key]:
                        return False
                    # 如果未进入上述判断语句，则将该格子的值添加至三个键中。
                    hash_map[row_key].append(elem)
                    hash_map[col_key].append(elem)
                    hash_map[sector_key].append(elem)

        # 循环完毕还没有冲突则说明该数独有效
        return True


class Solution:#用set  #看笔记
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row = defaultdict(set)
        col = defaultdict(set)
        small_square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] not in row[i] \
                            and board[i][j] not in col[j] \
                            and board[i][j] not in small_square[(i // 3, j // 3)]:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        small_square[(i // 3, j // 3)].add(board[i][j])
                    else:
                        return False
        return True


