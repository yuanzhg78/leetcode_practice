class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        1: 1
        2: 11
        3: 21
        4: 1211
        5: 111221
        """

        # 初始情况
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        # 记录上一拍的输出数据
        final = '11'

        for i in range(2, n):  # 对输入编号进行索引
            # 初始化参数
            out = ''  # out用来记录每次计算相同不同字符后得出的字符串
            last = final[0]  # 记录上个相同字符，初始值设置为第一个字符
            count = 1  # 记录相同的字符个数
            for c in final[1:]:  # 对上个字符串中的每个字符进行索引
                if c == last:
                    count += 1
                else:
                    out = out + str(count) + last
                    last = c
                    count = 1
            out = out + str(count) + last
            final = out
        return final