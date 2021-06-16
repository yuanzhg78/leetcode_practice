#二分查找第一次出现该数的下标
array = [1,2,3,4,5]
first = 0
last = len(array) #闭区间所以right不需要长度减1
def lower_bound (array, first, last, target):#返回[first,last)左闭右开区间内的第一个不小于value的值的位置
    while first < last: #搜索区间[first,last)不为空
        mid = first + (last - first) // 2 #寻找mid并且防止溢出
        if array[mid] < target:
            first = mid + 1
        else:
            last = mid
    return first #此处return last效果一样，因为[first,last)为空的时候重合


#两边都是闭区间的容易在return的时候出现错误


#算法导论中的方法 只适用于寻找出现的位置，并不能保证是第一次出现
#！！！！！！
# first = 0
# last = len(array) - 1
def binary_search (array, first, last, target):#返回[first,last)左闭右开区间内的第一个不小于value的值的位置
    while first < last: #搜索区间[first,last)不为空
        mid = first + (last - first) // 2
        if array[mid] < target:
            first = mid + 1
        elif array[mid] > target:
            last = mid - 1
        else:
            return mid
    return -1 #找不到target



