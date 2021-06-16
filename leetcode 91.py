# 如果当前位为0：
#
# 如果前一位不是1或2，则无法组成字母，整个串无法构成编码
# 如果前一位是1或者2，这时候构成的编码数目和之前相同的，因为只存在"10"或"20"的解码，即：dp[i] = dp[i-2] #因为1和0还有2和0不能拆
#
# 如果当前位不为0：
#
# 如果前一位和当前位能组成字母，则编码数目应该为前一位和前两位之和，即：dp[i] = dp[i-1] + dp[i-2]
# 如果前一位和当前位不能组成字母，则当前位单独组成字母，即dp[i] = dp[i-1]

#https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-fen-lei-tao-lun-by-user8973/

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if (s[i-1] == '1' or s[i-1] == '2'): #匹配“10”和“20”
                    dp.append(dp[-2])
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'): #匹配“1x”和“2x"情况，当然得小于26;
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
        return dp[-1]
