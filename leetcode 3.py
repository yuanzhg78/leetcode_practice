class Solution:  # index
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if len(s) < 2:
            return size
        dic = {}
        left = 0
        res = 1
        for right in range(size):
            #出现重复字符更新左边界 dic记录的是下标
            if s[right] in dic and dic[s[right]] >= left:
                left = dic[s[right]] + 1
            #更新结果
            res = max(res, right - left + 1)
            dic[s[right]] = right #每次迭代都要更新右边界
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        #更符合华东窗口的思想
        window=[]
        n=len(s)
        cur_len=0
        max_len=0
        for i  in range(n):
            val=s[i]
            #不管窗口里有没有都要把右边界的字母加进来
            if  val  not  in  window:
                window.append(val)
                cur_len+=1
            else:
                index=window.index(val)
                window=window[index+1:]
                window.append(val)
                cur_len=len(window)
            #判断结果需不需要更新
            if cur_len > max_len: max_len = cur_len
        return max_len



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 如果字符串s为空，返回0
        if not s:return 0
        # 保存窗口内字符串
        lookup = list()
        n = len(s)
        # 最大子串长度
        max_len = 0
        # 当前窗口长度
        cur_len = 0
        # 遍历字符串s
        for i in range(n):
            val = s[i]
            # 如果该值不在窗口中
            if not val in lookup:
                # 添加到窗口内
                lookup.append(val)
                # 当前长度+1
                cur_len+=1
            # 如果该值在窗口中已存在
            else:
                # 获取其在窗口中的位置
                index = lookup.index(val)
                # 移除该位置及之前的字符，相当于上图中的图3到图4
                lookup = lookup[index+1:]
                lookup.append(val)
                # 当前长度更新为窗口长度
                cur_len = len(lookup)
            # 如果当前长度大于最大长度，更新最大长度值
            if cur_len > max_len:max_len = cur_len
        # 返回最大子串长度
        return max_len

