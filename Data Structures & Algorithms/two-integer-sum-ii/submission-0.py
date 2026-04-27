class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans_list = []
        for index,element in enumerate(numbers):
            probe = target - element
            if probe in numbers:
                ans_list.append(index + 1)
                ans_list.append(numbers.index(probe)+ 1)
                break

        return ans_list