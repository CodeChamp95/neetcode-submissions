class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        max_seq_count = 1
        sequence = []
        
        for num in nums:
            if num in sequence:
                continue

            count = 1
            for i in range(1,len(nums)):
                if num+i in nums:
                    sequence.append(num+i)
                    count = count + 1
                else:
                    break
            
            if(count>max_seq_count):
                max_seq_count = count

        return max_seq_count


        