class Solution:
    def longestPalindrome(self, s: 'str') -> 'int':
        max_length = 0
        flag = 0
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
        for i in count.values():
            if i%2==0:
                max_length += i
            else:
                max_length += i -1
                flag = 1
        return max_length+flag
