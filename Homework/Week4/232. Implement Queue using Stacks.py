class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []   # For pushing elements
        self.stack_out = []  # For popping elements

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_out:
            # Transfer all elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.stack_out:
            # Transfer all elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()