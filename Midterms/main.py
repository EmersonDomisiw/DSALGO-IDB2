1.
class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    def push(self, item):
        self.item.append(item)
        print(f"Pushed item:", item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.item.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.item[-1]

    def len(self):
        return len(self.item)


S = Stack()

S.push(5)
S.push(3)
print("The current top of Stack: ", S.len())
print("Popped item: ", S.pop())
print("Is the stack empty? ", S.is_empty())
print("Popped item: ", S.pop())
print("Is the stack empty? ", S.is_empty())
try:
    S.pop()
except IndexError as e:
    print(e)
S.push(7)
S.push(9)
print("Top item: ", S.peek())
S.push(4)
print("The current top of Stack: ", S.len())
S.pop()
S.push(6)
S.push(8)
S.pop()




2.
class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    def push(self, item):
        self.item.append(item)
        print(f"Pushed item:", item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.item.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.item[-1]

    def len(self):
        return len(self.item)

S = Stack()

S.push(5)
S.push(3)
print("Popped: ", S.pop())
S.push(2)
S.push(8)
print("Popped: ", S.pop())
print("Popped: ", S.pop())
S.push(9)
S.push(1)
print("Popped: ", S.pop())
S.push(7)
S.push(6)
print("Popped: ", S.pop())
print("Popped: ", S.pop())
S.push(4)
print("Popped: ", S.pop())
print("Popped: ", S.pop())