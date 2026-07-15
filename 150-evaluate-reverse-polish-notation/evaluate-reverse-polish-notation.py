class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        n = len(tokens)
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                num2 = stk.pop()
                num1 = stk.pop()
                res = 0

                match token:
                    case '+':
                        res = num1 + num2
                    case '-':
                        res = num1 - num2
                    case '*':
                        res = num1 * num2
                    case '/':
                        res = int(num1 / num2)
                
                stk.append(res)
            else:
                stk.append(int(token))
        
        return stk[0]
                    
                        