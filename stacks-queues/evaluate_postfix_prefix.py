
import unittest

class Stack:
    def __init__(self):
        self.list = []

    def length(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

def evaluate_postfix(exp):
    if not exp:
        return None
    
    stack = Stack()
    operators = ['+','-','*','/']
    for i in range(0, len(exp)):
        if exp[i] not in operators:
            stack.push(exp[i])
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if exp[i] == '+':
                stack.push(op1+op2)
            elif exp[i] == '-':
                stack.push(op1-op2)
            elif exp[i] == '*':
                stack.push(op1*op2)
            elif exp[i] == '/':
                stack.push(op1/op2)
    return stack.pop()
    

def evaluate_prefix(exp):
    if not exp:
        return None

    stack = Stack()
    operators = ['+','-','*','/']
    for i in range(len(exp)-1, -1, -1):
        if exp[i] not in operators:
            stack.push(exp[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if exp[i] == '+':
                stack.push(op1+op2)
            elif exp[i] == '-':
                stack.push(op1-op2)
            elif exp[i] == '*':
                stack.push(op1*op2)
            elif exp[i] == '/':
                stack.push(op1/op2)       
    return stack.peek()   


class Test(unittest.TestCase):
    def setUp(self):
        self.postfix = [2,3,'*',5,4,'*','+',9,'-']
        self.prefix = ['-','+','*',2,3,'*',5,4,9]

    def test_evaluate_postfix(self):
        self.assertEqual(evaluate_postfix(self.postfix), 17)

    def test_evaluate_prefix(self):
        self.assertEqual(evaluate_prefix(self.prefix), 17)

if __name__=="__main__":
    unittest.main()