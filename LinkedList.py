from typing import Any


class LinkedList:
    def __init__(self, next=None, value=None):
        self.__next = next
        self.__value = value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
