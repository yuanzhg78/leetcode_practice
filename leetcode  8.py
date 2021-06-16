class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if not str:
            return 0
        i = 0
        if str[0] in ["-","+"]:
            i = 1
        #isdecimal字符串是否只包含十进制字符 (此处是当前位)
        if len(str[i:]) == 0 or not str[i].isdecimal():
            return 0
        while i < len(str):
            if not str[i].isdecimal():
                break
            i += 1
        str = int(str[:i])
        if str < -2**31:
            return -2**31
        if str > 2**31 -1:
            return 2**31 -1
        return str