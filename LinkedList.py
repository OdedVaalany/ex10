from __future__ import annotations
from typing import Any, List, Tuple

class Node:
    """
    Class Node is an implementation to a node in a linked list.
    Node has data and a pointer to the next Node.
    """
    def __init__(self, data: Tuple[int, int] = None, next: Node=None) -> None:
        """
        des: Node constructor creates a new node with data if recieved,
             and pointer to next Node if recieved.
        params: Node constructor creates a new node with data recieved
        """
        self.__data = data
        self.__next  = next

    def __str__(self) -> str:
        """
        return: string representation of Node's data
        """
        return str(self.__data)

    def get_data(self) -> Tuple[int, int]:
        """
        return: the Node's data
        """
        return self.__data

    def get_next(self) -> Node:
        """
        return: pointer to the next Node
        """
        return self.__next

    def set_data(self, data: Tuple[int, int]) -> None:        
        """
        des: set the Node's data to the data recieved
        params: data: the data to set
        """
        self.__data = data

    def set_next(self, next: Node) -> None:
        """
        des: set the next Node's data to the data recieved
        params: data: the data to set the next node with
        """
        self.__next = next


class LinkedList:
    """
    LinkedList class wrappes Node and provieds an API to use a linked 
    list of nodes.
    """
    def __init__(self, head: Node = None) -> None:
        """
        des: Node constructor creates a new list with node as head if
             recieved, otherwise head will be empty
        params: List constructor creates a new list with  the
                Node recieved as the head of the list
        """
        self.__head = head

    def get_head(self) -> Any:
        """
        return: List's head Node, None if list is empty
        """
        return self.__head

    def is_empty(self) -> bool:
        """
        return: True if list is empty, False otherwise
        """
        return self.__head == None

    def add(self, data: Tuple[int, int]) -> None:
        """
        des: adds a Node to the end of the list, with the node's data
             recieved as a param.
        params: data: the data to add to the list's tail
        """
        if self.is_empty():
            self.__head = Node(data)
            return
        if self.get_head().get_next() == None:
            self.get_head().set_next(Node(data))
            return
        
        iterator = self.get_head()
        
        while(iterator.get_next()):
            iterator = iterator.get_next()
        iterator.set_next(Node(data))
    
    def add_head(self, new_head: Tuple[int, int]) -> None:
        """
        des: adds a Node to the head of the list, with the node's data
             recieved as a param.
        params: new_head: the data to add to the list's head
        """
        nh = Node(new_head)
        nh.set_next(self.__head)
        self.__head = nh
        
    # def remove_head(self) -> None:
    #     """
    #     des: Removes the lists first cell
    #     """
    #     if self.is_empty():
    #         return None
        
    #     if self.get_head().get_next() == None:
    #         self.__head = None
    #         return None
        
    #     old_head = self.get_head()
    #     self.__head = self.__head.get_next()
    #     return old_head.get_data()
        
    def remove_tail(self) -> None:
        """
        des: Removes the lists last cell
        """
        if self.is_empty():
            return None
        
        if self.get_head().get_next() == None:
            self.__head = None
            return
        
        second_last = self.get_head()
        
        while(second_last.get_next().get_next()):
            second_last = second_last.get_next()
        second_last.set_next(None)
        
    def get_list(self) ->  List[Tuple[int, int]]:
        """
        return: a list of the snake's coordinates represnted
                by tuples
        """
        lst_data = []
        if self.is_empty():
            return []

        lst_data.append(self.get_head().get_data())
        
        iterator = self.get_head()
        
        while(iterator.get_next()):
            iterator = iterator.get_next()
            lst_data.append(iterator.get_data())
        

        return lst_data
    
    def remove_cell(self, key) -> None:
        """
        des: Removes the a cell from the list
        """
        temp = self.__head
 
        if (temp is not None):
            if (temp.get_data() == key):
                self.__head = temp.get_next()
                return
 
        while(temp is not None):
            if temp.get_data() == key:
                break
            prev = temp
            temp = temp.get_next()
 
        if(temp == None):
            return
 
        prev.set_next(temp.get_next())
 
        temp = None
