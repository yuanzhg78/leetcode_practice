'''
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

'''

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c_counter = collections.Counter(chars)
        result = 0
        for word in words:
            w_counter = collections.Counter(word)
            r = 0
            for w in w_counter:
                if w_counter[w] > c_counter[w]:
                    r = 0
                    break
                else:
                    r += w_counter[w]
            result += r
        return result


# from collections import Counter
# s = ‘abac’
# print(Counter(s))
# 输出结果为：{‘a’:2,‘b’:1,‘c’:1}

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for w in words:
            for i in w:
                if w.count(i) > chars.count(i):
                    break
            else:
                res += len(w)
        return res