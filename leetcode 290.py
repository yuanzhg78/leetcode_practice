class Solution:
    def wordPattern(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str_.split(' ')
        if len(pattern) != len(str_list):
            return False
        return len(set(zip(pattern, str_list))) == len(set(pattern)) == len(set(str_list))
