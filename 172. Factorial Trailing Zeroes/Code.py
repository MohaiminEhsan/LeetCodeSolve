class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n):
            if n==0:
                return 1
            else: 
                return n*factorial(n-1)
        
        n_fact = factorial(n)

        count = 0
        while True:
            if n_fact%10==0:
                count = count + 1
                n_fact = n_fact/10
            else:
                break

        return count
      
      


########## To avoid TLE:
class Solution:
  def trailingZeroes(self, n: int) -> int:
    return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
