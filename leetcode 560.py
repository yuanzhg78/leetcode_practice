#https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/ha-xi-biao-zhu-xing-jie-shi-python3-by-zhu_shi_fu/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = {0:1} #累加和最小为0
        sum = 0 #累加和
        count = 0 #出现次数

        for num in nums:
            sum += num
            if (sum-k) in dict:#sum正好等于0  #核心部分
                #若sum - k存在于hashhash中，说明存在连续序列使得和为k。则令count += hash[sum - k]
                #count += hash[sum−k]，表示sum - k出现几次，就存在几种子序列使得和为k。
                count += dict[sum-k]
            if sum in dict:
                dict[sum]+=1
            else:
                dict[sum] = 1
        return count




#借助哈希表保存累加和sum及出现的次数。若累加和sum-k在哈希表中存在，则说明存在连续序列使得和为k。则之前的累加和中，sum-k出现的次数即为有多少种子序列使得累加和为sum−k。
#此外，对于遇到的每个总和，我们还确定已经发生 sum-k总和的次数，因为它将确定具有总和 k 的子阵列发生到当前索引的次数。我们将 count增加相同的量。


#时间复杂度：O(n)。数组 nums仅需遍历一遍。

#空间复杂度：O(n)。哈希表 mapmap 在最坏情况下可能有 n个不同的键值。

