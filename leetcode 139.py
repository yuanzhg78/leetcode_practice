class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if (i>=len(word) and s[i-len(word):i]==word):
                    dp[i]=dp[i] or dp[i-len(word)]
        return dp[-1]



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):  # 第一层循环是字符串

            for word in wordDict:  # 循环每个dict，看是否能装进去

                if (i >= len(word) and s[i - len(word):i] == word):  # 这里注意，需要满足当前str[i-len(word):i]  的字符串正好等于dict中的字符串。
                    dp[i] = dp[i] or dp[i - len(word)]  # 取一个能装进去的就是True

        return dp[-1]




def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]


