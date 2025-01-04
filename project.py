class ExpressionEvaluator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(self, c):
        return c in self.operators

    def precedence(self, operator):
        return self.operators.get(operator, 0)

    def infix_to_postfix(self, expression):
        stack = []  # Stack to hold operators
        postfix = []  # Resultant postfix expression

        for char in expression:
            if char.isalnum():  # Operand
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('
            else:  # Operator
                while (stack and stack[-1] != '(' and
                       self.precedence(char) <= self.precedence(stack[-1])):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ''.join(postfix)

    def evaluate_postfix(self, postfix):
        stack = []

        for char in postfix:
            if char.isdigit():
                stack.append(int(char))
            else:  # Operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 // operand2)  # Integer division
                elif char == '^':
                    stack.append(operand1 ** operand2)

        return stack.pop()

 