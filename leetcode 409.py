s='abccccdd'


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        length = 0
        k = 0
        for s1 in s:
            if s1 not in dict:
                dict[s1] = 1
            else:
                dict[s1] += 1
        for value in dict.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                k = 1
        return length + k
