class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+","-","*","/"]
        resultado = 0

        for i in range(len(tokens)):
            if tokens[i] in operator:
                one = stack.pop()
                two = stack.pop()
                
                resultado = eval(f"{two} {tokens[i]} {one}" )
                result = int(resultado)
                stack.append(result)
            else:
                stack.append(tokens[i])

        return int(stack.pop())        