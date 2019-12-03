import stack
class MyQueue:
    def __init__(self):
        self.stack = stack.stack()
        self.rev = stack.stack()

    def push(self, data):
        while self.stack.top():
            self.rev.append(self.stack.pop()[0])
        self.stack.append(data)
        while self.rev.top():
            self.stack.append(self.rev.pop()[0])
        return

    def pop(self):
        while self.stack.top():
            self.rev.append(self.stack.pop()[0])

        top=self.rev.pop()
        while self.rev.top():
            self.stack.append(self.rev.pop()[0])

        return top

    def peek(self):
        '''Get the front element.'''
        while self.stack.top():
            self.rev.append(self.stack.pop()[0])

        top=self.rev.top()
        while self.rev.top():
            self.stack.append(self.rev.pop()[0])

        return top

    def empty(self):
        '''Returns whether the queue is empty.'''
        if self.stack.top():
            return True
        return False

