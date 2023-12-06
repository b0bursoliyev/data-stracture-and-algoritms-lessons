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

    def size(self):
        return len(self.stack)

    def pprint(self):
        for i in range(stack.size()):
            stack.peek()

stack = Stack()
print(stack.isEmpty())
print(stack.peek())
items = [1,5,4,8,9,5,6,4,8,5,6,2]
for i in items:
    stack.push(i)
print(stack.size())
a = stack.pop()
stack.push(a)
