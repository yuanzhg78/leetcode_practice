from collections import defaultdict
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        lamps = set([tuple(i) for i in lamps])
        cols = defaultdict(int)
        rows = defaultdict(int)
        add = defaultdict(int)
        sub = defaultdict(int)

        for i, j in lamps:
            rows[i] += 1
            cols[j] += 1
            add[i + j] += 1
            sub[i - j] += 1

        for x, y in queries:
            if rows[x] > 0 or cols[y] > 0 or add[x+y] > 0 or sub[x-y] > 0:
                res.append(1)
            else:
                res.append(0)
            for dx in [0, -1, 1]:
                for dy in [0, -1, 1]:
                    r, c = x + dx, y + dy
                    if (r, c) in lamps:
                        lamps.remove((r, c))
                        rows[r] -= 1
                        cols[c] -= 1
                        add[r + c] -= 1
                        sub[r - c] -= 1
        return res


class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        lamps_set = set()
        rows, cols, add, sub = {}, {}, {}, {}
        for i, j in lamps:
            rows[i] = rows.get(i, 0) + 1
            cols[j] = cols.get(j, 0) + 1
            add[i + j] = add.get(i + j, 0) + 1
            sub[i - j] = sub.get(i - j, 0) + 1
            lamps_set.add((i, j))

        for x, y in queries:
            if rows.get(x, 0) > 0 or cols.get(y, 0) > 0 or add.get(x + y, 0) > 0 or sub.get(x - y, 0) > 0:
                res.append(1)
            else:
                res.append(0)
            for dx in [0, -1, 1]:
                for dy in [0, -1, 1]:
                    r, c = x + dx, y + dy
                    if (r, c) in lamps_set:
                        lamps_set.remove((r, c))
                        rows[r] -= 1
                        cols[c] -= 1
                        add[r + c] -= 1
                        sub[r - c] -= 1
        return res


#https://leetcode-cn.com/problems/grid-illumination/solution/ji-ge-xiao-keng-by-suo-yi-ni-z/

from collections import defaultdict
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        cols = defaultdict(int)
        rows = defaultdict(int)
        hill_diagonals = defaultdict(int)
        dale_diagonals = defaultdict(int)

        lamp_set = set()
        for row, col in lamps:                 # 初始化，统计横竖对角线上灯的个数。
            cols[col] += 1
            rows[row] += 1
            hill_diagonals[row - col] += 1
            dale_diagonals[row + col] += 1
            lamp_set.add((row, col))            # 将灯的数组转化为字典

        def state(row, col):
            return bool(cols[col] + rows[row] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def turn_off(row, col):
            for i in [-1, 0, 1]:
                if 0 <= i + row < N:
                    for j in [-1, 0, 1]:
                        if 0 <= col + j < N:
                            if (i + row, j + col) in lamp_set:
                                lamp_set.remove((i + row, j + col))
                                cols[j + col] -= 1
                                rows[i + row] -= 1
                                hill_diagonals[row + i - j - col] -= 1
                                dale_diagonals[row + i + j + col] -= 1

        res = []
        for row, col in queries:
            res.append(int(state(row, col)))
            turn_off(row, col)
        return res
