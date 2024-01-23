#!/usr/bin/python3
"""Define classes for singly-linked list."""


class Node:
    """Represent node in singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize new node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The  next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, node):
        if type(node).__name__ != "Node" and node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = node


class SinglyLinkedList:
    """SinglyLinkedList"""

    def __init__(self):
        """Initialize a SinglyLinkedList instance."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node with the given value into the linked list.

        Args:
            value (Node): The new node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            crnt = self.__head
            while (crnt.next_node is not None and
                    crnt.next_node.data < value):
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node

    def __str__(self):
        """Generate a string representation of the linked list."""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return ('\n'.join(nodes))
