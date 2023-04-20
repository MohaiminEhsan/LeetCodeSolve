class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = 1
        number = 0
        for j in reversed(range(len(digits))):
            number = number + digits[j]*i
            i = i * 10

        number = number + 1

        digits2 = []

        while True:
            if number < 10:
                digits2.append(number)
                break
            new = number%10
            digits2.append(new)
            number = number/10
        digits2.reverse()
        return digits2
            
