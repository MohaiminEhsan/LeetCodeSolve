class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = 0

        l = len(nums)
        for i in range (0, l-1):
            for j in range(i+1,l):
                number = nums[i] + nums[j]
                print (i, j)
                print (number)
                if number == target:
                    index1= i
                    index2= j
                    break
                
        arr = [index1, index2]
        return arr
            



