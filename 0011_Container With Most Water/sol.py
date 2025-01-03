class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        j = len(height)-1
        i = 0
        while i < j:
            max_height = min(height[i],height[j])
            width = j - i
            max_water = max(max_water,(max_height * width))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return(max_water)