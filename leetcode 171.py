class Solution(object):
    def titleToNumber(self, s):
        ans = 0
        for i, c in enumerate(s):
            ans = ans*26 + ord(c)-ord('A')+1
        return ans


#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，
# 返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

#
# 标签：字符串遍历，进制转换
# 初始化结果ans = 0，遍历时将每个字母与A做减法，因为A表示1，所以减法后需要每个数加1，计算其代表的数值num = 字母 - ‘A’ + 1
# 因为有26个字母，所以相当于26进制，每26个数则向前进一位
# 所以每遍历一位则ans = ans * 26 + num
# 以ZY为例，Z的值为26，Y的值为25，则结果为26 * 26 + 25=701
# 时间复杂度：O(n)
