class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        strarr = []
        for i in range(1,n+1):
            arr.append(i)

        for i in arr:
            if i%3==0 and i%5==0:
                strarr.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                strarr.append("Fizz")
            elif i%3!=0 and i%5==0:
                strarr.append("Buzz")
            else:
                strarr.append(str(i))
        
        return strarr
