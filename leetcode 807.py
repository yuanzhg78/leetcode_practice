class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:

        N = len(grid)  # Height
        M = len(grid[0])  # Width

        # Transpose grid: Interchange rows and columns
        grid_t = zip(*grid)
        #print(list(grid_t))
        #[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        #[(3, 2, 9, 0), (0, 4, 2, 3), (8, 5, 6, 1), (4, 7, 3, 0)]


        # Vertical and horizontal skylines
        sk_v = [max(row) for row in grid]  # As seen from left/right
        sk_h = [max(row) for row in grid_t]  # As seen from top/bottom

        res = 0
        for i in range(N):  # Rows of original grid
            for j in range(M):  # Columns of original grid
                # The new building cannot be higher than either skylines
                diff = min(sk_h[j], sk_v[i]) - grid[i][j]
                res += diff
        return res


if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]

    #pre = createTree(pre)
    #post=createTree(post)
    res=Solution().maxIncreaseKeepingSkyline(grid)