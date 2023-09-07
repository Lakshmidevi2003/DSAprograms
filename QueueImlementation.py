from collections import  deque

class Queue:
    def __int__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

q = Queue()
q.enqueue({
    'company': "wall mart",
    'timestamp': "15",
    "price": 20
})
"""q.enqueue(10)
q.enqueue(15)
q.enqueue(20)"""
print(q)