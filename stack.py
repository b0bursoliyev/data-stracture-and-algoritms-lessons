class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        return 'Done'

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stack[-1]

stack = Stack()
print(stack.isEmpty())
print(stack.peek())
print(stack.push(5))
print(stack.push(2))
print(stack.pop())
