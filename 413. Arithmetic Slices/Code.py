class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
    
        l = len(nums)
        index = 0
        for i in nums:
            if index<2:
                arr.append(0)
            else:
                if nums[index]-nums[index-1] == nums[index-1]-nums[index-2]:
                    arr.append(arr[index-1]+1)
                else:
                    arr.append(0)
            index = index+1
        total = 0
        for i in arr:
            total = total + i
        
        return total
