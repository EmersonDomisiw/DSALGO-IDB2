"""
def dequeue(self):
    if self.is_empty():
        raise Exception('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():
        self._tail = None
    return answer

class LinkedQueue:

    #---------------- nested _Node class ----------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #--------------- queue methods ----------------
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

if __name__ == "__main__":

    Q = LinkedQueue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)

    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())

    try:
        print(Q.dequeue())
    except Exception as e:
        print(e)





from LinkedStack import LinkedStack as Stack
from PositionalList import PositionalList as PositionalList

stack = Stack()
plist = PositionalList()

plist.add_first(1)
plist.add_first(5)
plist.add_first(8)
plist.add_first(2)
plist.add_first(3)
plist.add_first(0)
plist.add_first(11)

print("The Current values in the Positional List:")
for element in plist:
    print(element)

def sort_asc(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walker = marker
                while walker != L.first() and L.before(walker).element() > value:
                    walker = L.before(walker)
                L.delete(pivot)
                L.add_before(walker, value)

sort_asc(plist)
print("The Sorted lIst in Ascending:")
for element in plist:
    print(element)

def sort_desc(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            number = L.after(marker)
            value = number.element()
            if value < marker.element():
                marker = number
            else:
                walker = marker
                while walker != L.first() and L.before(walker).element() < value:
                    walker = L.before(walker)
                L.delete(number)
                L.add_before(walker, value)

sort_desc(plist)
print("The Sorted List in Descending:")
for element in plist:
    print(element)


from LinkedStack import LinkedStack as Stack
from PositionalList import PositionalList as PositionalList

op_stack = Stack()

def op_prio(op):
    '''Returns priority of the operator.'''
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

def convert_infix_to_postfix(expression):
    '''Convert infix expression to postfix notation.'''
    result = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for sign in tokens:
        if sign.isdigit() or sign.isidentifier():
            result.append(sign)
        elif sign == '(':
            op_stack.push(sign)
        elif sign == ')':
            while not op_stack.is_empty() and op_stack.top() != '(':
                result.append(op_stack.pop())
            if not op_stack.is_empty():
                op_stack.pop()
        else:
            while (not op_stack.is_empty() and
                   op_prio(op_stack.top()) >= op_prio(sign)):
                result.append(op_stack.pop())
            op_stack.push(sign)

    while not op_stack.is_empty():
        result.append(op_stack.pop())
    return ' '.join(result)
"""

from collections import deque
from LinkedStack import LinkedStack as Stack
from PositionalList import PositionalList as PositionalList

plist = PositionalList()
plist.add_first(1)
plist.add_first(5)
plist.add_first(8)
plist.add_first(2)
plist.add_first(3)
plist.add_first(0)
plist.add_first(11)

print("The Current values in the Positional List:")
for element in plist:
    print(element)


def sort_asc(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walker = marker
                while walker != L.first() and L.before(walker).element() > value:
                    walker = L.before(walker)
                L.delete(pivot)
                L.add_before(walker, value)

sort_asc(plist)
print("The Sorted List in Ascending Order:")
for element in plist:
    print(element)

def sort_desc(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            number = L.after(marker)
            value = number.element()
            if value < marker.element():
                marker = number
            else:
                walker = marker
                while walker != L.first() and L.before(walker).element() < value:
                    walker = L.before(walker)
                L.delete(number)
                L.add_before(walker, value)

sort_desc(plist)
print("The Sorted List in Descending Order:")
for element in plist:
    print(element)

queue = deque()

queue.append(1)
queue.append(5)
queue.append(8)
queue.append(2)
queue.append(3)
queue.append(0)
queue.append(11)


print("\nProcessing elements from the queue (FIFO):")
while queue:
    print(queue.popleft())

op_stack = Stack()

def op_prio(op):
    '''Returns priority of the operator.'''
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

def convert_infix_to_postfix(expression):
    '''Convert infix expression to postfix notation.'''
    result = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for sign in tokens:
        if sign.isdigit() or sign.isidentifier():
            result.append(sign)
        elif sign == '(':
            op_stack.push(sign)
        elif sign == ')':
            while not op_stack.is_empty() and op_stack.top() != '(':
                result.append(op_stack.pop())
            if not op_stack.is_empty():
                op_stack.pop()
        else:
            while (not op_stack.is_empty() and
                   op_prio(op_stack.top()) >= op_prio(sign)):
                result.append(op_stack.pop())
            op_stack.push(sign)

    while not op_stack.is_empty():
        result.append(op_stack.pop())
    return ' '.join(result)