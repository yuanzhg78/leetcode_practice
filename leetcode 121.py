class Solution(object):#双指针法，一次遍历
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        pro = 0
        minpr = prices[0]
        for p in prices:  # 直接遍历
            pro = max(pro, p - minpr) #更新最大高度差，即收益
            minpr = min(minpr, p) #最低值
        return pro

#找到状态转移方程：res = max(res, prices[i] - min_val);，res为前i天的最大收益，min_val为前i天的最小值。
#初始化状态量：res = 0;, min_val = INT_MAX;

#其实两种都算是动态规划，都是记录之前的值，来更新当前的值。第一种更好理解，记录最低值，不断更新最大高度差。
#思路二: 动态规划, 我们可以遍历数组, 记录前面最小的价格, 用当天价格减去最小价格, 一定是这天可以获得最大利润!
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return res

