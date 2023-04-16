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
        for i in range (0, l):
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
           

            
# ==============> this gives TLE For some reason

        ls = len(nums)
        for i in range(ls):
            for j in range(i + 1, ls):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                
                
# ------------------> For less time Complexity





