class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        start = 0
        end = len(height) - 1

        while start < end:
            smaller_bar = min(height[start], height[end])
            smaller_bar_index = start if smaller_bar == height[start] else end

            if smaller_bar_index == start:
                start = start + 1
                # visited_bars = []
                while(height[start] < smaller_bar):
                    sum = sum + (smaller_bar - height[start])
                    start = start + 1

            else:
                end = end - 1
                # visited_bars = []
                while(height[end] < smaller_bar):
                    sum = sum + (smaller_bar - height[end])
                    end = end - 1

        return sum

                