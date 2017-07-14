from src.structures import Stack


class MaxStack(Stack):
    def getMax(self):
        currentMax = self.pop()
        while not self.isEmpty():
            currentMax = max(currentMax, self.pop())
        return currentMax
