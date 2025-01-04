# Expressionevaluator
# Expression Evaluator

This Python class `ExpressionEvaluator` provides two core functionalities for evaluating mathematical expressions:

1. **Infix to Postfix Conversion**: Converts infix expressions (e.g., `A+B*C`) to postfix notation (e.g., `ABC*+`).
2. **Postfix Evaluation**: Evaluates a postfix expression (e.g., `53+2*`) and returns the result.

## Features
- Supports basic operators: `+`, `-`, `*`, `/`, `^`.
- Handles parentheses for grouping operations in infix expressions.
- Converts infix expressions to postfix notation using the Shunting Yard algorithm.
- Evaluates postfix expressions using a stack-based approach.
