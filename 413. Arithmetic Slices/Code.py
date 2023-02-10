class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        temp1 = 1
        temp2 = 1
        temp11 = 1
        temp22 = 1
        l = len(nums)
        for i in range(1,l+1):
            temp1 = temp1*i
        for i in range(1,l):
            temp2 = temp2*i
        for i in range(1,l-3+1):
            temp11 = temp11*i
        for i in range(1,l-3):
            temp22 = temp22*i
        
        fact1 = temp1 / (6*temp11)
        fact2 = temp2 / (6*temp22)

        return fact1-fact2
