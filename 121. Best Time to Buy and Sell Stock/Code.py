class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        min1 = 0
        for i in range(0, l-1):
            for j in range (i, l-1):
                if prices[i]>=prices[j]:
                    continue
                else:
                    min2 = prices[j]-prices[i]
                    if min2>min1:
                        min1 = min2
        
        print(min1)
        return min1
