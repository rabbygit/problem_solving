# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

import collections


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque()
        self.addInteger(nestedList)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return True if len(self.queue) else False

    def addInteger(self, nestedList: [NestedInteger]):
        for num in nestedList:
            if num.isInteger():
                self.queue.append(num.getInteger())
            else:
                self.addInteger(num.getList())