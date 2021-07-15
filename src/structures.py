"""Helpful data structures not implemented in Python"""

from typing import Any, Optional


class Queue():
    def __init__(self, items: Optional[list] = None):
        """Standard FIFO Queue
        :param items: Items (in order) to enqueue
        """
        if items is not None:
            self.list = items
        else:
            self.list = []
    
    def enqueue(self, other: Any):
        """Enqueue `other` to the Queue"""
        self.list.append(other)
    
    def dequeue(self) -> Any:
        """Dequeue item, if items exist"""
        if len(self.list):
            return self.list.pop(0)
        return None

    def peek(self) -> Any:
        """Peek front of Queue"""
        return self.list[0]
    
    def __len__(self) -> list:
        return len(self.list)


class Stack():
    def __init__(self, items: Optional[list] = None):
        """Standard FILO Stack
        :param items: Items (in order) to push
        """
        if items is not None:
            self.list = items
        else:
            self.list = []

    def push(self, other: Any):
        """Push `other` to the Stack"""
        self.list.append(other)
    
    def pop(self) -> Any:
        """Pop item, if items exist"""
        if len(self.list):
            return self.list.pop()
        return None
    
    def peek(self) -> Any:
        """Peek top of Stack"""
        return self.list[-1]

    def __len__(self) -> list:
        return len(self.list)
    

