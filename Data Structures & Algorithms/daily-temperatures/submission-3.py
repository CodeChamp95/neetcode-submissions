class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans_list = []
        # i = len(temperatures) - 1
        lst = []
        top = -1
        for i in range(len(temperatures) - 1, -1, -1):
            num = temperatures[i]
            # print(f"Entering while loop with top as {top} and i as {i}")
            while top != -1 and temperatures[lst[top]] <= num:
                lst.pop()
                top -= 1

            if top == -1:
                ans_list.append(0)
                top += 1
                lst.append(i)
                # i -= 1
                continue
            else:
                top += 1
                lst.append(i)
                diff = lst[top - 1] - lst[top]
                ans_list.append(diff)
            # i -= 1
        new_ans_list = []
        i = len(temperatures) - 1
        while i >= 0:
            new_ans_list.append(ans_list[i])
            i -= 1


        # for i in range(len(temperatures) - 1):
        #     count = 0
        #     for j in range(i+1,len(temperatures)):
        #         count += 1
        #         if temperatures[j] > temperatures[i]:
        #             ans_list.append(count)
        #             break
        #         if j == len(temperatures) - 1:
        #             count = 0
        #             ans_list.append(count)
        # ans_list.append(0)
        return new_ans_list
