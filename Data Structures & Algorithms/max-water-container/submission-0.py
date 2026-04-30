class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                smaller_bar = min(heights[i],heights[j])
                res = smaller_bar * (j-i)
                if res > max:
                    max = res

        return max 