class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_elements = []
        for i in range(0,len(nums)):
            if nums[i] in visited_elements:
                return True
            visited_elements.append(nums[i])

        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[j] == nums[i]):
        #             return True
        
        return False
        