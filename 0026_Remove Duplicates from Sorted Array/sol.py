class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0

        while i < len(nums):
            if nums[i] == nums[k]:
                i += 1
            else:
                k += 1
                nums[k] = nums[i]
        # add 1 to k since k is not index but number of unique elements
        k += 1
        return k