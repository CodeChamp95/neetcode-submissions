class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print("hello")

        for row in board:
            nums_checked = []
            for num in row:
                if num in nums_checked:
                    print("Row check failed")
                    return False
                elif(num != "."):
                    nums_checked.append(num)

        for col in range(9):
            nums_checked = []
            for row in range(9):
                num = board[row][col]
                if num in nums_checked:
                    print("Column check failed")
                    return False
                elif(num != "."):
                    nums_checked.append(num)

        
        nums_checked = []
        for row in range(3):
            for col in range(3):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    print("checking")
                    print(f"First, the repeated number is {num}")
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

            
        nums_checked = []
        for row in range(3):
            for col in range(3,6):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    print(f"Second, the repeated number is {num}")
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)


        nums_checked = []
        for row in range(3):
            for col in range(6,9):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    print(f"Third, the repeated number is {num}")
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(3,6):
            for col in range(3):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num !="."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(3,6):
            for col in range(3,6):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(3,6):
            for col in range(6,9):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(6,9):
            for col in range(3):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(6,9):
            for col in range(3,6):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)

        nums_checked = []
        for row in range(6,9):
            for col in range(6,9):
                num = board[row][col]
                print(f"The number is {num}")
                if num in nums_checked:
                    return False
                elif(num != "."):
                    nums_checked.append(num)
                    print(nums_checked)


        return True