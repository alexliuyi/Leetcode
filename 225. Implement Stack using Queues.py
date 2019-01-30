class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp_queue = list()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.temp_queue.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = self.temp_queue.pop()
        return x
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        x = self.temp_queue[-1]
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.temp_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
