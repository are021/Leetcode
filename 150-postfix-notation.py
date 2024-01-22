
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        operators = {'+', '-', '*', '/'}

        for t in tokens:
            if t in operators:
                n2 = numbers.pop()
                n1 = numbers.pop()

                if t == '+':
                    numbers.append(n1 + n2)
                
                if t == '-':
                    numbers.append(n1 - n2)
                
                if t == '*':
                    numbers.append(n1 * n2)
                
                if t == '/':
                    numbers.append(int(n1 / n2))
            else:
                numbers.append(int(t))
        
        return numbers.pop()

