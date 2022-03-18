#Stack

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.stack)
print(s.peek())
print(s.size())
print(s.is_empty())
s.pop()
print(s.stack)
print(s.peek())
print(s.size())
print(s.is_empty())