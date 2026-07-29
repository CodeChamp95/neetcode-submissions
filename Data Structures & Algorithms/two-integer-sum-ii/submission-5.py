class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ans_list = []
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
                # break

            elif numbers[start] + numbers[end] < target:
                start = start + 1

            else: end = end - 1

        return []