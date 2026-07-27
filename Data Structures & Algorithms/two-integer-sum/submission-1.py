class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set()
        ans_list = []

        for i in range(len(nums)):
            nums_set.add(nums[i])

        second_num = 0
        for i in range(len(nums)):
            y = target - nums[i]
            if y in nums_set:
                second_num = y
                ans_list.append(i)
                print("Appended in answer")
                break

        for i in range(len(nums)):
            if nums[i] == second_num:
                ans_list.append(i)
                print("Appended in answer")
                break

        return ans_list

        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j] == target):
        #             ans_list.append(i)
        #             ans_list.append(j)
        #             return ans_list
        