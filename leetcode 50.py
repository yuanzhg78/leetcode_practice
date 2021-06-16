class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        i = abs(n)
        while i != 0:
            if i % 2 == 1:
                res *= x
            x *= x
            i //= 2
        return res if n>0 else 1/res
#加倍的次数正好等于减半的次数


if __name__ == '__main__':
    x=4.00
    n=3

    solution = Solution()
    result = solution.myPow(x,n)
    print(result)



#for循环的次数,即i作减半直到为1的次数
#而x *= x;相当于对幂作加倍，加倍的次数正好等于减半的次数。
#但是由于i/2在i为奇数时会造成损失，
#损失量刚好是上一次的x值(可以自己举例推导一下)，需要把这个值乘到res里面做弥补，
#同时最后一次i/2必然为1即奇数，所以最终得到的x和损失量相乘得到最终结果

