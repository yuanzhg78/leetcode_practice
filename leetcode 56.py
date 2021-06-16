def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #先把intervals按照第一个值进行排序
    intervals.sort()
    n = len(intervals)
    if n == 0:
        return [] 
    result = [intervals[0]]
    for i in range(1,n):
        #此时必有重合，则重合区间的右值为最大的那个
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1],intervals[i][1])
        #无重合则直接添加区间
        else:
            result.append(intervals[i])
    return result




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            while i < n - 1 and intervals[i+1][0] <= right:
                i += 1
                right = max(intervals[i][1], right)
            res.append([left, right])
            i += 1
        return res

class Solution:#最终版本
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        n=len(intervals)
        i=0
        while i<n:
            left=intervals[i][0]
            right=intervals[i][1]
            while i<n-1 and intervals[i+1][0]<=right:
                i+=1
                right=max(intervals[i][1],right)

            res.append([left,right])
            i+=1
        return res