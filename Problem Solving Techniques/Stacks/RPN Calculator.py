"""
Write a small program that computes arithmetic expressions in postfix notation, also known as reverse polish notation or RPN.

● Use whichever language you want (advice: use the one you know the best!)
● Do it on your laptop in your favorite development environment.
● Use of internet isn’t allowed. Only use your knowledge and the help your editor gives you. If you have questions, you can
ask the interviewer.

In postfix notation, parentheses and operator priorities are not necessary: an operator always applies to its immediately
preceding arguments. For instance, consider the expression "6 8 4 + 3 2 + - *".

● The first operator "+" is applied to its preceding arguments, which are 8 and 4, giving 12. The subexpression "8 4 +" is then
replaced by its result 12, so the expression becomes "6 12 3 2 + - *".
● The next operator "+" is applied to its arguments, which are 3 and 2, giving 5. The subexpression "3 2 +" is replaced by 5, so
the expression becomes "6 12 5 - *".
● The next operator "-" is applied to its arguments, which are 12 and 5, giving 7. The subexpression "12 5 -" is replaced by 7,
so the expression becomes "6 7 *".
● The next operator "*" is applied to its arguments, that is 6 and 7, giving 42. The subexpression "6 7 *" is replaced by 42, so
the expression becomes "42".
● When all operators have been applied, the expression has become its result: 42.
Your program must support the following operators:
● binary operators: +, -, *, /
● unary operator: sqrt (square root)
Hint: One way to evaluate such expression is to use a stack to store intermediate results.

This can be a simple program in text mode, no need for a user interface. If you use Unix, you may get the input from the
command-line arguments. Don’t handle input errors - assume it will be valid.
Input                      Result
3 4 2 + *                      18
5 4 2 * 3 + + sqrt             4
3.12 4 + 2 *                 14.24

"""

import math
def rpn_calculator(str):
      
      str = str.split(' ')
      
      operators = {'+': lambda a,b:a+b , 
                   '-': lambda a,b:a-b ,
                   '*': lambda a,b: a * b ,
                   '/': lambda a,b: a / b ,
                   'sqrt': lambda a: math.sqrt(a)
                  }

      st = []
      for i in str:
            if i not in operators.keys():
                  st.append(float(i))
            else:
                  if i != 'sqrt':
                        result = operators[i](float(st.pop()) , float(st.pop()))
                        st.append(result)
                  else:
                        result = operators[i](float(st.pop()))
                        st.append(result)
      return st.pop()
                  
                  
print(rpn_calculator('5 4 2 * 3 + + sqrt'))
print(rpn_calculator('16 15 16 sqrt + -'))
