class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_list = []
        first_value = 1
        first_value_special = 1
        array_map = {}

        for i in range(len(nums)):
            array_map[nums[i]] = array_map.get(nums[i],0) + 1

        for i in range(1,len(nums)):
            first_value *= nums[i]

        if nums[0] == 0:
            ans_list.append(first_value)
            for i in range(1,len(nums)):
                ans_list.append(0)
            return ans_list

        for i in range(1,len(nums)):
            if nums[i] == 0:
                continue
            first_value_special *= nums[i]

        ans_list.append(first_value)        
        for i in range(1,len(nums)):
            array_map[nums[i]] = array_map.get(nums[i],0) - 1
            if nums[i] == 0 and array_map[nums[i]] == 0:
                res = first_value_special * nums[0]
                ans_list.append(res)
            elif nums[i] == 0 and array_map[nums[i]] > 0:
                ans_list.append(0)
            else:
                res = (first_value/nums[i]) * nums[0]
                ans_list.append(int(res))
            # for j in range(len(nums)):
            #     if(j == i):
            #         continue

            #     res = res * nums[j]
            # ans_list.append(res)

        return ans_list     