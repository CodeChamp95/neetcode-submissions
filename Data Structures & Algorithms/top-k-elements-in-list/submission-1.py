class Solution:

    def find_max_freq_element(self, nums: List[int]):
        max_freq_element = nums[0]
        max_freq = 1
        unchecked_elements = []

        for element in nums:
            unchecked_elements.append(element)

        for i in range(0,len(nums)-1):
            if(nums[i] not in unchecked_elements):
                continue

            freq = 1
            for j in range(i+1,len(nums)):
                if(nums[j] == nums[i]):
                    freq = freq + 1
                    unchecked_elements.remove(nums[j])
            
            if(freq > max_freq):
                max_freq = freq
                max_freq_element = nums[i]
            unchecked_elements.remove(nums[i])

        return max_freq_element,max_freq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_list = []
        # original_size = len(nums)
        for i in range(1,k+1):
            print("The array sent is: ")
            for element in nums:
                print(element)
            max_freq_element, max_freq = self.find_max_freq_element(nums)
            print(f"Element received is {max_freq_element}")
            ans_list.append(max_freq_element)

            for j in range(1,max_freq + 1):
                for element in nums:
                # print(f"We have reached index {index} where we have element {element}")

                    if(element == max_freq_element):
                        nums.remove(element)
                        break

        return ans_list
        