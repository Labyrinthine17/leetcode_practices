class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums_size = len(nums)

        if nums_size == 0:
            return []
        
        summary = []
        start_val = nums[0]
        end_val = nums[0]

        for i in range(1, nums_size):
            print("start_val = ",start_val, " end_val =",end_val)
            if nums[i] == end_val + 1:
                end_val = nums[i]
            else:
                if start_val == end_val:
                    summary.append(str(start_val))
                else:
                    summary.append(str(start_val) + "->" + str(end_val))
                start_val = nums[i]
                end_val = nums[i]

        if start_val == nums[-1]:
            summary.append(str(start_val))
        else:
            summary.append(str(start_val) + "->" + str(end_val))

        return summary