class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return len(nums)
        begin = 0
        up    = 1
        down  = 2
        state = begin
        max_length = 1
        for i in range(1,len(nums)):
            if state == begin:
                if nums[i-1] < nums[i]:
                    state = up
                    max_length +=1
                elif nums[i-1] > nums[i]:
                    state = down
                    max_length +=1
            if state == up:
                if nums[i-1] > nums[i]:
                    state = down
                    max_length +=1
            if state == down:
                if nums[i-1] < nums[i]:
                    state = up
                    max_length +=1    
            i+=1
        return max_length
