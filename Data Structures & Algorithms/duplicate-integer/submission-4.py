class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_elements = []
        for i in range(0,len(nums)):
            if nums[i] in visited_elements:
                return True
            visited_elements.append(nums[i])

        return False
        