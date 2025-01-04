class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        k = 10**5 + 1
        for j, val in enumerate(nums):
            total += val
            while total >= target:
                k = min(k, j-i+1)
                total -= nums[i]
                i += 1

        if k > 10**5:
            k = 0

        return k