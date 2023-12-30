#!/usr/bin/python3
# module contans class defination


class Node:
    """ represent "node" class defination"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrive data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """ set value to data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer\n")

    @property
    def next_node(self):
        """retrive value of next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set value to next node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object\n")


class SinglyLinkedList:
    """ represent singlylinkedlist class"""
    def __init__(self):
        """Initialize a new Node."""
        self.__head = None

    def sorted_insert(self, value):
        """ insert new node to list"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if self.__head and value <= self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        lists = []
        current = self.__head
        while current:
            lists.append(str(current.data))
            current = current.next_node
        return "\n".join(lists)
