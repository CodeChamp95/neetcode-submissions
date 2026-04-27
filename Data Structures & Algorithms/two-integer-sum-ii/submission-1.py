class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ans_list = []
        # for index,element in enumerate(numbers):
        #     probe = target - element
        #     if probe in numbers:
        #         ans_list.append(index + 1)
        #         ans_list.append(numbers.index(probe)+ 1)
        #         break

        # return ans_list

        ans_list = []
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                ans_list.append(start + 1)
                ans_list.append(end + 1)
                break

            elif numbers[start] + numbers[end] < target:
                start = start + 1

            else: end = end - 1

        return ans_list