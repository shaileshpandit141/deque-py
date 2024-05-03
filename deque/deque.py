from typing import Any, NoReturn, Union


class Node:
    """### Implementation of Node."""

    def __init__(self, item: Any, prev: Union[None, object] = None, next: Union[None, object] = None ) -> None:
        # Assign to self object.
        self.item: Any = item
        self.prev: Union[None, object] = prev
        self.next: Union[None, object] = next

    def __repr__(self) -> str:
        return f"Node({self.item})"


class Deque:
    """### Usage
    #### Create an object of Deque class.
    ```python
    deque: Deque = Deque()
    ```

    Now you can able to perform this operation on deque object.

    #### 1. Insertion and Deletion
    * `insert_front(data):` Insert an element at the front of the deque.
    * `insert_rear(data):` Insert an element at the rear of the deque.
    * `delete_front():` Delete an element from the front of the deque.
    * `delete_rear():` Delete an element from the rear of the deque.

    #### 2. Get Front and Rear Elements
    * `is_empty():` Check if the deque is empty.
    * `size():` Get the current size of the deque.

    For Example:
    ```python
    # Insert elements
    deque.insert_front(10)
    deque.insert_front(0)
    deque.insert_rear(20)
    deque.insert_rear(30)

    # Output deque status
    print("Deque element:", deque)
    print("Size of Deque:", len(deque))
    print("Front element:", deque.get_front())
    print("Rear element:", deque.get_rear())

    # Delete elements
    deque.delete_front()
    deque.delete_rear()

    # Output deque status after deletion
    print("Deque element:", deque)
    print("Size of Deque:", len(deque))
    print("Front element:", deque.get_front())
    print("Rear element:", deque.get_rear())
    ```"""

    def __init__(self) -> None:
        # Assign to self object.
        self.__front: Union[None, object] = None
        self.__rear: Union[None, object] = None
        self.__item_count: int = 0

    @property
    def font(self) -> NoReturn:
        raise AttributeError("'Deque' has no attribut 'font'.")
    
    @property
    def rear(self) -> NoReturn:
        raise AttributeError("'Deque' has no attribut 'rear'.")
    
    @property
    def item_count(self) -> NoReturn:
        raise AttributeError("'Deque' has no attribut 'item_count'.")
        
    def is_empty(self) -> bool:
        """### Return True if 'Deque' is not empty otherwise False.
        For example:
        ```python
        deque: Deque = Deque()
        print(deque.is_empty())
        O/P -> False
        ```"""
        return self.__front is None
    
    def insert_front(self, data: Any) -> None:
        """### Insert item into font of the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_font(20)
        deque.insert_font(30)
        print(deque)
        O/P -> [ 20 30 ]
        ```"""
        node: Node = Node(data)
        node.prev = None
        node.next = self.__front
        if self.is_empty():
            self.__rear = node
        else:
            if isinstance(self.__front, Node):
                self.__front.prev = node
        self.__front = node
        self.__item_count += 1

    def insert_rear(self, data: Any) -> None:
        """### Insert item into rear of the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        print(deque)
        O/P -> [ 30 20 ]
        ```"""
        node: Node = Node(data)
        node.prev = self.__rear
        node.next = None
        if self.is_empty():
            self.__front = node
        else:
            if isinstance(self.__rear, Node):
                self.__rear.next = node
        self.__rear = node
        self.__item_count += 1

    def delete_front(self) -> None:
        """### Delete font element in the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_font(20)
        deque.insert_font(30)
        deque.delete_front()
        print(deque)
        O/P -> [ 20 ]
        ```"""
        if self.is_empty():
            return None
        if self.__front == self.__rear:
            self.__front = None
            self.__rear = None
        else:
            if isinstance(self.__front, Node):
                self.__front = self.__front.next
            if isinstance(self.__front, Node):
                self.__front.prev = None
        self.__item_count -= 1

    def delete_rear(self) -> None:
        """### Delete rear element in the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        deque.delete_front()
        print(deque)
        O/P -> [ 20 ]
        ```"""
        if self.is_empty():
            return None
        if self.__front == self.__rear:
            self.__front = None
            self.__rear = None
        else:
            if isinstance(self.__rear, Node):
                self.__rear = self.__rear.prev
            if isinstance(self.__rear, Node):
                self.__rear.next = None
        self.__item_count -= 1

    def get_font(self) -> Any:
        """### Return font item if 'Deque' is not empty otherwise None.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_font(20)
        deque.insert_font(30)
        print(deque.get_font())
        O/P -> 30
        ```"""
        if self.is_empty():
            return None
        else:
            if isinstance(self.__front, Node):
                return self.__front.item
            return None
    
    def get_rear(self) -> Any:
        """### Return rear item if 'Deque' is not empty otherwise None.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        print(deque.get_font())
        O/P -> 30
        ```"""
        if self.is_empty():
            return None
        else:
            if isinstance(self.__rear, Node):
                return self.__rear.item
            return None
    
    def size(self) -> int:
        """### Return the size of the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        print(deque.size())
        O/P -> 2
        ```"""
        return self.__item_count
        
    def __len__(self) -> int:
        """### Return the size of the 'Deque'.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        print(len(deque))
        O/P -> 2
        ```"""
        return self.__item_count
    
    def __repr__(self) -> str:
        """### Return the string representation of 'Deque' if you print the object of 'Deque' class.
        For example:
        ```python
        deque: Deque = Deque()
        deque.insert_rear(20)
        deque.insert_rear(30)
        print(deque)
        O/P -> [ 30 20 ]
        ```"""
        temp = self.__front
        if isinstance(temp, Node):
            print("[", end=" ")
            while temp.next is not None:
                print(temp.item, end=" ")
                if isinstance(temp.next, Node):
                    temp = temp.next
            print(temp.item, end=" ")
        return f"]"
    