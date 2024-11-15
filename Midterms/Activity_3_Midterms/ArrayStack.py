
class ArrayStack:
    def _init_ (self):
        self.data = []

    def len_ (self):
        return len(self.data)

    def _is_empty (self):
        return len (self)

    def push(self,val):
        self.data.append(val)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()




