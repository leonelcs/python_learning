class Node:
    name = None
    _left = None
    _right = None

    def left(self):
        return self._left

    def right(self):
        return self._right

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

class Tree:
    root: Node


