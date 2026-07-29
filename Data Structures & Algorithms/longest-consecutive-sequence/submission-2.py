class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        max_seq_count = 1
        # sequence = set()
        empt = set()

        for num in nums:
            empt.add(num)
        
        for num in empt:
            if num - 1 in empt:
                continue

            count = 1
            for i in range(1,len(nums)):
                if num+i in empt:
                    count = count + 1
                else:
                    break
            
            if(count>max_seq_count):
                max_seq_count = count

        return max_seq_count


        