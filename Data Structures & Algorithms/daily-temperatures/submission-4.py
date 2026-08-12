class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans_list = []
        lst = []
        top = -1
        for i in range(len(temperatures) - 1, -1, -1):
            num = temperatures[i]
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
        new_ans_list = []
        for i in range(len(temperatures) - 1, -1, -1):
            new_ans_list.append(ans_list[i])

        return new_ans_list
