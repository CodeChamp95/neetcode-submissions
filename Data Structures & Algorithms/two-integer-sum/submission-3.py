class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set()
        hash_map = {}
        ans_list = []

        for i in range(len(nums)):
            nums_set.add(nums[i])
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        second_num = 0
        first_index = -1
        for i in range(len(nums)):
            y = target - nums[i]
            if hash_map[nums[i]] == 1:
                nums_set.remove(nums[i])
            if y in nums_set:
                second_num = y
                first_index = i
                ans_list.append(i)
                print("Appended in answer")
                break

        for i in range(len(nums)):
            if nums[i] == second_num and i != first_index:
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
        