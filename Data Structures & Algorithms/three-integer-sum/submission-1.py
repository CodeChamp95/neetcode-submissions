class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp

        for num in nums:
            print(num)

        target = 0
        ans_list = []
        for index in range(len(nums) - 2):
            num = nums[index]
            target = num * (-1)
            print(f"the two sum target is {target}")
            start = index + 1
            end = len(nums) - 1

            while(start < end):
                sum = nums[start] + nums[end]
                if sum == target:
                    print("Sum reached")
                    new_list = [num,nums[start],nums[end]]
                    if new_list not in ans_list:
                        ans_list.append(new_list)
                    start = start + 1
                    end = end - 1

                elif sum > target:
                    end = end - 1

                else: start = start + 1

        return ans_list