class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l= len(strs)

        str_com = ""

        i_range = len(strs[0])

        for i in range(i_range):
            temp = strs[0][i]
            flag="match"
            for j in range(l):
                if len(strs[j])>=i+1:
                    if temp!=strs[j][i]:
                        temp==""
                        flag="no match"
                        break
                    else:
                        flag="match"
                else:
                    flag="no match"
                    break
            if flag=="match":
                str_com = str_com + temp
            elif flag=="no match":
                break
        return str_com
