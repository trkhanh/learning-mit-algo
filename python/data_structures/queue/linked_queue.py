""" A Queue using a linked list like structure """
from typing import Any


class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.net = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedQueue:
    def __init__(self) -> None:
        self.front = self.rear = None

    def __iter__(self):
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        return len(self) == 0

    def put(self, item) -> None:
        node = Node(item)
        if self.is_empty():
            self.front = self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def get(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.data

    def clear(self) -> None:
        self.front = self.rear = None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
