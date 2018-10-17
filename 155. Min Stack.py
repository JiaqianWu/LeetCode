# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:26:20 2018

@author: wujiaqian
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        self.minList = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min == None:
            self.min = x
        elif  self.min > x:
            self.min = x
        self.minList.append(self.min)

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[:-1]
        self.minList = self.minList[:-1]
        if self.minList == []:
            self.min = None
        else:
            self.min = self.minList[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minList != []:
            return self.minList[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
print(obj.min)
print(obj.minList)
obj.push(0)
print(obj.min)
print(obj.minList)
obj.push(6)
print(obj.min)
print(obj.minList)
param_1 = obj.getMin()
param_2 = obj.pop()
print(obj.stack)
#param_3 = obj.top()
#print(param_3)
param_4 = obj.getMin()
print(param_1,param_2,param_4)