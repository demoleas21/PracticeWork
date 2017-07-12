class Stack:
    def __init__(self):
        self.container = []

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def stackSize(self):
        return len(self.container)

    def isEmpty(self):
        return self.container == []

    def peek(self):
        return self.container[len(self.container) - 1]

    def showStack(self):
        return self.container


class QueueTwoStacks:
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


def main():
    queue = QueueTwoStacks()
    queue.enqueue(1)
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.enqueue(2)
    print queue.showStacks()
    queue.enqueue(3)
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.enqueue(4)
    print queue.showStacks()
    queue.enqueue(5)
    print queue.showStacks()
    queue.enqueue(6)
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.enqueue(7)
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.enqueue(8)
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()
    queue.dequeue()
    print queue.showStacks()


if __name__ == '__main__':
    main()
