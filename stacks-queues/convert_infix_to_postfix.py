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


def infix_to_postfix(exp):
    if not exp:
        return None

    stack = Stack()
    operators = ['*','/','+','-']
    open_paren = '('
    close_paren = ')'
    postfix = []
    for i in range(0, len(exp)):
        if exp[i] not in operators and exp[i]!=open_paren and exp[i]!=close_paren:
            postfix.append(exp[i])
        elif exp[i] == open_paren:
            stack.push(open_paren)
        elif exp[i] == close_paren:
            c = stack.length()
            while c > 0 and stack.peek() != "(":
                postfix.append(stack.pop())
                c -= 1
            stack.pop()
        else:
            c = stack.length()
            while c > 0 and stack.peek() in operators:
                top = stack.peek()
                if top in operators and precedance(top, exp[i]):
                    postfix.append(stack.pop())      
                c -= 1      
            stack.push(exp[i])
    while stack.length() > 0:
        postfix.append(stack.pop())
    return postfix

def precedance(op1, op2):
    operators = ['*','/','+','-']
    if operators.index(op1) < operators.index(op2):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def setUp(self):
        self.infix_noparen = ['a','+','b','*','c','-','d','*','e']
        self.infix_withparen = ['(','(','a','+','b',')','*','c','-','d',')','*','e']

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix(self.infix_noparen),['a','b','c','*','+','d','e','*','-'])
        self.assertEqual(infix_to_postfix(self.infix_withparen),['a','b','+','c','*','d','-','e','*'])


if __name__=="__main__":
    unittest.main()

