from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        prefix = defaultdict(int)
        n = len(wall)
        for i in range(0, n):
            cur_sum = 0
            for j in range(0, len(wall[i]) - 1):
                #计算prefix sum并更新哈希表
                cur_sum += wall[i][j]
                prefix[cur_sum] += 1
        #异常test [[1],[1],[1]] 在循环j的时候直接退出了。所以val里没有东西。需要添加默认值
        return n - max(prefix.values(), default=0)


if __name__ == '__main__':
            #nums = [1, 1, 2]
            s = [[1],[1],[1]]
            solution = Solution()
            result = solution.leastBricks(s)
            print(result)

# 怎么找到每行的砖块都恰好对齐的那些缝隙呢?
# 可以用额外的存储空间来辅助一下~, 比如 Hashmap
# 怎么把计算对齐的缝隙转化成可操作的代码呢?
# 计算每一行砖块宽度的前缀和! 在计算某一行砖块的时候, 将砖块的宽度和进行累计, 每一个累计砖块的宽度和都作为 hashmap 的 key, value就是这个key出现的次数.
# 怎么求穿过的最少砖块数?
# 一个垂直的线最多穿过的砖块数就是这堵墙的行数, 减去出现次数/频数最高的砖块的宽度和, 就相当于找到了砖块对齐的缝隙最多的那一条垂直线了!


#res2 = min(a, key=lambda x: abs(x))
