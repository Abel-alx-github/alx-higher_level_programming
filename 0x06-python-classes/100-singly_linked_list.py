#!/usr/bin/python3
# module contans class defination


class Node:
    """ represent "node" class defination"""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self._data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self._head is None:
            self._head = new
            return
        if self._head and value <= self._head.data:
            new.next_node = self._head
            self._head = new
            return
        current = self._head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        lists = []
        current = self._head
        while current:
            lists.append(str(current.data))
            current = current.next_node
        return "\n".join(lists)
