class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if c == ')' or c == '}' or c == ']':
                if len(stack)==0:
                    return False
                elif c == ')':
                    test = stack.pop()
                    if test != '(':
                        return False
                        break
                elif c == '}':
                    test = stack.pop()
                    if test != '{':
                        return False
                        break
                elif c == ']':
                    test = stack.pop()
                    if test != '[':
                        return False
                        break
        if len(stack)==0:
            return True
        else:
            return False
        
