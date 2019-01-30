class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()
        self.min  = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if len(self.min)==0:
            self.min.append(x)
        else:
            if x > self.min[-1]:
                x = self.min[-1]
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        x = self.data[-1]
        return x
        

    def getMin(self):
        """
        :rtype: int
        """
        x = self.min[-1]
        return x
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
