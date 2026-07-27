class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_set = set()
        for i in range(len(nums)):
            if nums[i] in visited_set:
                return True
            visited_set.add(nums[i])

        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[j] == nums[i]):
        #             return True
        
        return False
        