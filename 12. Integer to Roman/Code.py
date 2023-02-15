class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        while True:
            if num/1000>=1 or num/900>=1:
                if num/1000>=1:
                    for i in range(int(num/1000)):
                        str = str + "M"
                    num = num%1000
                elif num/900>=1:
                    for i in range(int(num/900)):
                        str = str + "CM"
                    num = num%900
            elif num/500>=1 or num/400>=1:
                if num/500>=1:
                    for i in range(int(num/500)):
                        str = str + "D"
                    num = num%500
                elif num/400>=1:
                    for i in range(int(num/400)):
                        str = str + "CD"
                    num = num%400
            elif num/100>=1 or num/90>=1:
                if num/100>=1:
                    for i in range(int(num/100)):
                        str = str + "C"
                    num = num%100
                elif num/90>=1:
                    for i in range(int(num/90)):
                        str = str + "XC"
                    num = num%90
            elif num/50>=1 or num/40>=1:
                if num/50>=1:
                    for i in range(int(num/50)):
                        str = str + "L"
                    num = num%50
                elif num/40>=1:
                    for i in range(int(num/40)):
                        str = str + "XL"
                    num = num%40
            elif num/10>=1 or num/9>=1:
                if num/10>=1:
                    for i in range(int(num/10)):
                        str = str + "X"
                    num = num%10
                elif num/9>=1:
                    for i in range(int(num/9)):
                        str = str + "IX"
                    num = num%9
            elif num/5>=1 or num/4>=1:
                if num/5>=1:
                    for i in range(int(num/5)):    
                        str = str + "V"
                    num = num%5
                elif num/4>=1:
                    for i in range(int(num/4)):
                        str = str + "IV"
                    num = num%4
            elif num/1>=1:
                for i in range(int(num/1)):
                    str = str + "I"
                break
            else:
                break
        return str
