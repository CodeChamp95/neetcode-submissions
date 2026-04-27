class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_list = []
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if(j == i):
                    continue

                res = res * nums[j]
            ans_list.append(res)

        return ans_list     