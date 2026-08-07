class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        top = -1
        open_symbols = "([{"
        close_symbols = ")]}"
        open_set = set(open_symbols)
        close_set = set(close_symbols)
        for symbol in s:
            if symbol in open_set:
                lst.append(symbol)
                top += 1
            elif symbol in close_set:
                if top == -1:
                    return False
                elif (symbol == ')' and lst[top] == '(') or (symbol == ']' and lst[top] == '[') or (symbol == '}' and lst[top] == '{'):
                    # print("Got equality")
                    lst.pop(top)
                    top -= 1
                else: return False
        
        return top == -1