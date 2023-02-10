class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        total = 0
        arr= []
        for i in s:
            if i=='I':
                arr.append(I)
            elif i=="V":
                arr.append(V)
            elif i=="X":
                arr.append(X)
            elif i=='L':
                arr.append(L)
            elif i=='C':
                arr.append(C)
            elif i=='D':
                arr.append(D)
            elif i=='M':
                arr.append(M)
        
        index = 0
        total = 0
        for n in arr:
            l = len(arr)
            if arr[index]!=0:
                if index<l-1:
                    if arr[index]<arr[index+1]:
                        total = total + arr[index+1] - arr[index]
                        arr[index+1] = 0
                        arr[index] = 0
                    else: 
                        total = total + arr[index]
                        arr[index] = 0    
                else:
                    total = total + arr[index]
                    arr[index] = 0
            index = index + 1
        return total
