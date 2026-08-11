class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        top = -1
        operators = "+-*/"
        operator_set = set(operators)
        res = 0
        for token in tokens:
            if token not in operator_set:
                lst.append(int(token))
                top += 1
            else:
                # print("Entered operand section")
                opnd1 = lst.pop()
                top -= 1
                opnd2 = lst.pop()
                top -= 1

                if token == "+":
                    res = opnd1 + opnd2
                    lst.append(res)
                    top += 1
                elif token == "-":
                    res = opnd1 - opnd2
                    lst.append(res)
                    top += 1
                elif token == "*":
                    res = opnd1 * opnd2
                    lst.append(res)
                    top += 1
                else:
                    res = opnd1/opnd2
                    lst.append(res)
                    top += 1
        
        return res