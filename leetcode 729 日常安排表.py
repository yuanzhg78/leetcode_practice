# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。
#
# MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
#
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。
#
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
#
# 请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

#二分查找
class MyCalendar:
    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        left, right = 0, len(self.arr)-1
        while left <= right:
            mid = (left+right) // 2
            if not (end-1 < self.arr[mid][0] or start >= self.arr[mid][1]):
                return False
            if self.arr[mid][0] > start:
                right = mid - 1
            else:
                left = mid + 1
        self.arr.insert(left, [start, end])
        return True


#暴力法 穷举 利用栈 stack
# 暴力解法：检查新区间与已有的区间是否重合，如果重合则返回False;如果不重合，则更新日历，返回True;
# 一开始是逐天检查，超时；改进以后逐区间检查，节省了时间；
# 检查的方法是遍历记录，新区间（start, end）对每一个记录都应该有right<=start or end<=left，否则出现重合

class MyCalendar:

    def __init__(self):
        self.calendar = []

    # 建立日程列表

    def book(self, start: int, end: int) -> bool:
        #如果是空的直接加
        if not self.calendar:
            self.calendar.append((start, end))
            return True
        else:
            #直接遍历里面的两个元素 如果符合区间。直接添加
            for l, r in self.calendar:
                if l >= end or r <= start:  # 判断区间是否为有效区间
                    pass
                else:
                    return False
            self.calendar.append((start, end))
            return True
