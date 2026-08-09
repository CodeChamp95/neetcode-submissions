class MinStack:

    def __init__(self):
        self.first1 = -1
        self.lst1 = []
        self.first2 = -1
        self.lst2 = []
        # self.min_number = 2^31

    def push(self, val: int) -> None:
        self.first1 += 1
        self.lst1.append(val)
        if self.first2 == -1:
            self.first2 += 1
            self.lst2.append(val)
        else:
            self.lst2.append(min(self.lst2[self.first2],val))
            self.first2 += 1
        # self.min_number = min(self.min_number, val)
        
    def pop(self) -> None:
        if self.first1 != -1:
            self.lst1.pop(self.first1)
            self.first1 -= 1
        if self.first2 != -1:
            self.lst2.pop(self.first2)
            self.first2 -= 1

    def top(self) -> int:
        return self.lst1[self.first1]
        
    def getMin(self) -> int:
        # print("the stack is: ")
        # self.display()
        return self.lst2[self.first2]

    # def display(self):
    #     for i in range(self.first + 1):
    #         print(self.lst[i])
        
