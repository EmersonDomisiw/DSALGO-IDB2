
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def first(self):
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __init__(self):
        self.queue = []

#This is the code that is in the table.
Q = Queue()

print("First sequence of operations:")
Q.enqueue(5)
print("Enqueued is: 5")
Q.enqueue(3)
print("Enqueued is: 3")
print("Length of Q:", len(Q))
print("Dequeued is:", Q.dequeue())
print("Is Q empty?", Q.is_empty())
print("Dequeued is:", Q.dequeue())
print("Is Q empty?", Q.is_empty())
Q.enqueue(7)
print("Enqueued is: 7")
Q.enqueue(9)
print("Enqueued is: 9")
print("First element:", Q.first())
Q.enqueue(4)
print("Enqueued is: 4")
print("Length of Q:", len(Q))
print("Dequeued is:", Q.dequeue())
"""

#Code in the second.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
        print(f"enqueue({e}): Queue is now: {self.queue}")

    def dequeue(self):
        if not self.queue:
            return None
        value = self.queue.pop(0)
        print(f"dequeue(): Returns {value}, Queue is now: {self.queue}")
        return value

print("\nSecond sequence of operations:")
Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
Q.dequeue()  
Q.enqueue(2)
Q.enqueue(8)
Q.dequeue()  
Q.dequeue()  
Q.enqueue(9)
Q.enqueue(1)
Q.dequeue()  
Q.enqueue(7)
Q.enqueue(6)
Q.dequeue()  
Q.dequeue()  
Q.enqueue(4)
Q.dequeue()  
Q.dequeue()  
"""