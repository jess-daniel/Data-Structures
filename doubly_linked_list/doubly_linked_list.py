"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    # delete for node itself
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #  create instance of list node with value
        new_node = ListNode(value)
        # increment the DLL length attribute 
        self.length += 1
        # check if DLL is empty
        if self.length == 0:
            # if empty - 
                # set head and tail to new node instance
            self.head = new_node
            self.tail = new_node
        else:
            # if not empty - 
                # set new node's next to current head
                # set head prev to new node
                # set head to new node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store value of head
        head = self.head
        # decrement the len of DLL
        self.length -= 1
        # delete the head
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
            # if head.next is not none 
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to none
                # set tail to none
        # return the value
        return head.value

        # value = self.head.value
        # self.delete(self.head)
        # return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #  create instance of list node with value
        new_node = ListNode(value)
        # increment the DLL length attribute 
        self.length += 1
        # check if DLL is empty
        if self.length == 0:
        # if not self.tail and not self.tail.head
            # if empty - 
                # set head and tail to new node instance
            self.head = new_node
            self.tail = new_node
        else:
            # if not empty - 
                # set new node's prev to current tail
            new_node.prev = self.tail
                # set tail's next to new node
            self.tail.next = new_node
                # set tail to new node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail = self.tail.value
        self.delete(self.tail)
        return tail
        # store value of tail
        # decrement the len of DLL
        # delete the tail
            # if tail.prev is not none 
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to none
                # set tail to none
        # return the value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value