class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """       
        self.temp.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x = self.temp[0]
        self.temp.remove(self.temp[0])
        return x
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        x = self.temp[0]
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.temp)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
