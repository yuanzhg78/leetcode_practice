#用栈解决,把当前目录压入栈中,遇到..弹出栈顶,最后返回栈中元素.
#用栈来维护路径。便于”..”时出栈的要求。
# 本题最大的坑点是”.”和”..”能与其它字母组成目录名称。比如”..home”。
# 在明确这点后，那么”/”就是唯一的分割符了。
# 当遇到”/”时，将连续的多个”/”全部取出来。多个”/”压缩到一个”/”，输入栈中。

#一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for i in path.split('/'):
            if i not in ['', '.', '..']:
                stack.append(i)
            elif i == '..' and stack:
                stack.pop()
        return "/" + "/".join(stack)