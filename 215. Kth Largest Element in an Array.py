import heapq as hq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return hq.nlargest(k,nums)[-1]
