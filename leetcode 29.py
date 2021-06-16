#https://leetcode-cn.com/problems/divide-two-integers/solution/liang-shu-xiang-chu-pythonjie-ti-si-lu-wei-yun-sua/
#使用位运算
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_num = pow(2,31) - 1
        min_num = -pow(2,31)
        if dividend == min_num and divisor == -1:
            return max_num
        if divisor == -1:
            return -dividend
        if divisor == 1:
            return dividend
        flag = False if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else True
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor
        return self.helper(dividend,divisor,0,1) if flag else -self.helper(dividend,divisor,0,1)

    def helper(self,dividend,divisor,result,times):
        if dividend == divisor:
            return 1 if result == 0 else result + 1
        if dividend > divisor:
            if times == 1: return result
            return self.helper(dividend, divisor >> 1, result, times >> 1)
        if dividend < divisor:
            return self.helper(dividend - divisor, divisor << 1, result + times, times << 1)





class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_num = -pow(2, 31)
        max_num = pow(2, 31) - 1
        # 这些是特殊情况
        if dividend == min_num and divisor == -1: return  max_num
        if divisor == -1: return -dividend
        if divisor == 1: return dividend
        # 取负数正数的时候要特别注意一下 min_num(−2^31) 因为会溢出
        # 所以我们把正数变成负数，这样就不用担心溢出了
        # 先判断一下之前的符号问题，因为后面统一符号了
        sameSymbol = False if ( dividend > 0 and divisor < 0 ) or ( dividend < 0 and divisor >0 ) else True
        if dividend > 0: dividend = -dividend
        if divisor > 0: divisor = -divisor
        return self.divideMain(dividend, divisor, 0, 1) if sameSymbol else -self.divideMain(dividend, divisor, 0, 1)

    def divideMain(self, dividend, divisor, result, times):
        """
        计算主体
        : param result: 最后返回的结果
        ：param times: 计算时的临时倍数
        """
        # 当被除数与除数相等时，判断是否是第一次相减
        if dividend == divisor: return 1 if result == 0 else result + 1
        # 当 被除数 大于 除数 时（此时二者都为负数，其实就是正数的单被除数小于除数时）进行除数的 /2 操作
        if dividend > divisor:
            if times == 1: return result
            return self.divideMain(dividend, divisor >> 1, result, times >> 1)
        # 当 被除数 小于 除数 时（此时二者都为负数，其实就是正数的单被除数大于除数时）进行除数的 *2 操作
        if dividend < divisor:
            return self.divideMain(dividend-divisor, divisor << 1, result + times, times << 1)

