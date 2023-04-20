class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newNums = []
        for i in nums:
            if i not in newNums:
                newNums.append(i)
        
        for i in range(0,len(newNums)-1):
            nums[i] = newNums[i]
        print(nums)
        return len(newNums)
      
      #======================> for some reason, getting error

############Correct one

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1
