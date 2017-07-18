from src.structures import Stack


class QueueTwoStacks(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if not self.stack1.isEmpty() and self.stack2.isEmpty():
            while self.stack1.stackSize() > 1:
                self.stack2.push(self.stack1.pop())
            self.stack1.pop()

        elif not self.stack2.isEmpty():
            self.stack2.pop()

    def showStacks(self):
        return self.stack1.showStack(), self.stack2.showStack()
