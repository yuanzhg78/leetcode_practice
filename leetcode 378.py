class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        l, h = matrix[0][0], matrix[n - 1][m - 1]

        while l < h:
            count = 0
            mid = l + (h - l) // 2
            for i in range(n):
                j = m - 1
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
                # print(count, k)
            if count >= k:
                h = mid
            else:
                l = mid + 1
        return l

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high=matrix[n-1][m-1]
        while low < high:
            count = 0
            mid = low+(high-low)//2
            for i in range(n):
                j=m-1
                while j>=0 and matrix[i][j]>mid:
                    j-=1
                count+=j+1
            if count>=k:
                high=mid
            else:
                low=mid+1
        return low


if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]
    matrix = [
        [1, 5, 9],
        [10, 11, 13]

    ]
    k=8

    #pre = createTree(pre)
    #post=createTree(post)
    res=Solution().kthSmallest(matrix,k)


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def findOrd(matrix, val):
            order = 0
            for row in matrix:
                for col in row:
                    if col <= val: order += 1
            return order

        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            order = findOrd(matrix, mid)
            if order >= k:
                r = mid
            else:
                l = mid + 1
        return l