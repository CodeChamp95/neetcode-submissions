class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        start = 0
        end = len(heights) - 1

        while start < end:
            smaller_bar = min(heights[start], heights[end])
            smaller_bar_index = start if smaller_bar == heights[start] else end
            res = (end - start) * smaller_bar
            if res > max:
                max = res
            
            if smaller_bar_index == start:
                start = start + 1
            else: end = end - 1

        return max