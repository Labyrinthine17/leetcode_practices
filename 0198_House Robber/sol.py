class Solution:
    def rob(self, nums: List[int]) -> int:  
        n = len(nums)

        if n == 1:
            return nums[0]

        max_value_before = max(nums[0],nums[1])
        max_value_2_before = nums[0]

        for idx,val in enumerate(nums):
            if idx > 1:
                curr_max = max(max_value_2_before + val , max_value_before)
                
                max_value_2_before = max_value_before
                max_value_before = curr_max

        return(max_value_before) 