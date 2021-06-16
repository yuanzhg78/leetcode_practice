class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        start = 0
        total = 0
        n = len(gas)
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return -1 if total + tank < 0 else start
    #如果总共的汽油小于总共的消耗,是无解的