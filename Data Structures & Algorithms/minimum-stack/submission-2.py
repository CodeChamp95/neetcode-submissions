class MinStack:

    def __init__(self):
        self.first = -1
        self.lst = []
        # self.min_number = 2^31

    def push(self, val: int) -> None:
        self.first += 1
        self.lst.append(val)
        # self.min_number = min(self.min_number, val)
        
    def pop(self) -> None:
        if self.first != -1:
            self.lst.pop(self.first)
            self.first -= 1

    def top(self) -> int:
        return self.lst[self.first]
        
    def getMin(self) -> int:
        # print("the stack is: ")
        # self.display()
        min_num = 2^31
        for element in self.lst:
            min_num = min(min_num, element)
        return min_num 

    def display(self):
        for i in range(self.first + 1):
            print(self.lst[i])
        
