class BinaryTree:
    '''Binary Tree class for handling expressions.'''

    class Node:
        '''A node in the binary tree.'''

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None

    def set_root(self, root):
        '''Set the root of the tree.'''
        self._root = root

    def preorder(self):
        '''Generate preorder traversal of the tree.'''
        stack = []

        def _preorder(node):
            if node:
                stack.append(node._element)
                _preorder(node._left)
                _preorder(node._right)

        _preorder(self._root)
        return stack

    def inorder(self):
        '''Generate inorder traversal of the tree.'''
        stack = []

        def _inorder(node):
            if node:
                _inorder(node._left)
                stack.append(node._element)
                _inorder(node._right)

        _inorder(self._root)
        return stack

    def postorder(self):
        '''Generate postorder traversal of the tree.'''
        stack = []

        def _postorder(node):
            if node:
                _postorder(node._left)
                _postorder(node._right)
                stack.append(node._element)

        _postorder(self._root)
        return stack

def precedence(op):
    '''Return the precedence of operators.'''
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def shunting_yard(expression):
    '''Convert infix expression to postfix using the Shunting Yard algorithm.'''
    out = []
    ops_stack = []

    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isalnum():
            out.append(char)

        elif char == '(':
            ops_stack.append(char)

        elif char == ')':
            while ops_stack and ops_stack[-1] != '(':
                out.append(ops_stack.pop())
            ops_stack.pop()

        elif char in '+-*/^':
            while (ops_stack and precedence(ops_stack[-1]) >= precedence(char)):
                out.append(ops_stack.pop())
            ops_stack.append(char)

        i += 1

    while ops_stack:
        out.append(ops_stack.pop())

    return out

def build_expression_tree(postfix):
    '''Build a binary tree from a postfix expression.'''
    stack = []
    for token in postfix:
        if token.isalnum():
            stack.append(BinaryTree.Node(token))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(BinaryTree.Node(token, left, right))
    return stack[-1]

def main():
    equations = [
        "(3 * 5) - ((4 * 5) + (6 - 7))",
        "((a + b) * c) - (d - e)",
        "((a ^ b) + (c + d)) + ((e * f) / (g + h))",
        "(a + b) / (c * (d - (e ^ f)))",
        "((a - b) + c) * ((d + e) * (f / g))",
        "(((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1))) * 8"
    ]
    for i, equation in enumerate(equations, 1):
        print(f"Equation {i}: {equation}")
        postfix = shunting_yard(equation)
        print("Traversal Expression:", ''.join(postfix))

        tree = BinaryTree()
        root = build_expression_tree(postfix)
        tree.set_root(root)

        preorder_result = tree.preorder()
        inorder_result = tree.inorder()
        postorder_result = tree.postorder()

        print("Preorder Traversal (Stack):", " -> ".join(preorder_result))
        print("Inorder Traversal (Stack):", " -> ".join(inorder_result))
        print("Postorder Traversal (Stack):", " -> ".join(postorder_result))
        print()

if __name__ == '__main__':
    main()