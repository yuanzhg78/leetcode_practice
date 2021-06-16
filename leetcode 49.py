class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dic:
                dic[key] = [s]  # key对应一个列表 ！！字典中存储列表
            else:
                dic[key].append(s)  # 字典里用了列表，所以可以append
        return list(dic.values())  # 强制类型为list

