
#https://leetcode-cn.com/problems/decode-string/solution/pythonzhan-by-mai-mai-mai-mai-zi/
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        res = ''
        for i, s in enumerate(s):
            if s != ']':#不是右括号就可以进栈
                stack.append(s)
            else:
                string = ''
                while not stack[-1].isnumeric():
                    string = stack.pop()+string #除了数字以外的字母和括号放到string里
                times = ''
                while stack and stack[-1].isnumeric():
                    times = stack.pop() + times
                if times:
                    string = string[1:]*int(times)
                if stack:
                    stack.append(string)
                else:
                    res += string
        return res+''.join(stack)
if __name__ == '__main__':
            #nums = [1, 1, 2]
            s = "3[a]2[bc]"
            solution = Solution()
            result = solution.decodeString(s)
            print(result)

#
# # 华为的一道算法题：
# #
# # 读入一个字符串str，输出字符串str中的连续最长的数字串。
# #
# # 输入：abcd12345ed125ss123456789              输出：123456789
#
# x = input()
# curlen, curstr, maxlen, maxstr = 0, '', 0, ''
#
# for i, v in enumerate(x):
#     if v.isnumeric():
#         curlen += 1
#         curstr += v
#         if curlen > maxlen:
#             maxlen = curlen
#             maxstr = curstr
#     else:
#         curlen = 0
#         curstr = ''
# print(maxstr)
#


#https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
#本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

