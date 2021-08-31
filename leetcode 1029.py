class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # [[20, 10], [100, 50]]

        costs.sort(key=lambda x: x[1] - x[0])
        print(costs)
        mid = len(costs) // 2
        res = 0
        for i in range(mid):
            res += costs[i][1]
        for j in range(mid, len(costs)):
            res += costs[j][0]
        return res


class Solution:
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: (x[0]-x[1]))  # 计算去A地和去B低的费用差，然后按照费用差排序
        length_costs = len(costs)
        result = 0
        result += sum([i[0] for i in costs[:length_costs//2]])  # 前半部分去A地
        result += sum([i[1] for i in costs[length_costs//2:]])  # 后半部分去B地
        return result


# 假设将所有人都飞往b城市，则总费用为sum(costs[0...i][1])，定义总费用为sum;
# const sum = 0;
# const length = costs.length;
# for(int i=0;i < length;i++) {
# sum += costs[i][1];
# }
# 此时就相当于部分飞往a城市的人使用了飞往b城市的价格
# 但是根据题目要求，飞往a城市必须使用a城市的价格，且要求总费用要最低
# 所以要让总费用尽可能最低，则a城市的价格必须要尽可能低于b城市的价格。
# 所以我们使用b城市的价格减去a城市的价格，根据价格差值来从大到小进行排序。
# 则前n个数据的差值尽可能最大，即前n个人去往a城市的价格更低。

