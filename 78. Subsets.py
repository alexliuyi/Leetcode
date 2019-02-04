class Solution:
    def subsets(self, nums):
        result = []
        all_set = 1<<len(nums)
        for i in range(all_set):
            item =list()
            for j in range(len(nums)):
                if i & 1<<j:
                    item.append(nums[j])
            result.append(item)
        return result
        
