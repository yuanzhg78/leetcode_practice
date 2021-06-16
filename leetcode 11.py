class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        contain = 0
        while l < r:
            contain = max(contain, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return contain
#用两个指针一个在头一个在尾，计算P(i,j)容纳水的大小然后，将短的一侧向内部移动然后重新计算P(i,j)更新最大值，直到两个指针相遇。