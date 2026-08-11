class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans_list = []
        for i in range(len(temperatures) - 1):
            count = 0
            for j in range(i+1,len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    ans_list.append(count)
                    break
                if j == len(temperatures) - 1:
                    count = 0
                    ans_list.append(count)
        ans_list.append(0)
        return ans_list
