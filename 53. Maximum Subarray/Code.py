class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        max = -999999999
        for i in range(l):
            total = 0
            for j in range(i,l):
                total = total + nums[j]
                if total > max:
                    max = total
        return max
                


        
################# To avoid TLE:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        dp version (Detailed Explanation is available at 
        https://medium.com/@edward.zhou/leet-code-53-maximum-subarray-detailed-explained-python3-solution-d91c7affc02a )                
        '''
        dp = []
        dp.append(nums[0])
        current_largest_sum = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[i] > current_largest_sum:
                current_largest_sum = dp[i]
        return current_largest_sum
