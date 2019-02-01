class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        S = []
        result=""
        for i in range(len(num)):
            number = int(num[i])
            while len(S)!=0 and S[-1]>number and k>0:
                S.pop()
                k-=1
            if number!=0 or len(S)!=0:
                S.append(number)
        while len(S)!=0 and k>0:
            S.pop()
            k-=1
        for i in range(len(S)):
            result = result+str(S[i])          
        if result == "":
            result="0"    
        return result
