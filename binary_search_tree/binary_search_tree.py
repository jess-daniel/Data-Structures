from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # case 1: value is < self.value
        if value < self.value:
            # if no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # else
            else:
                self.left.insert(value) 
                # repeat process on left subtree (call insert again => self.insert(value)) 
        # case 2: value is >= self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # case 1: self.value == target
        if self.value == target:
            return True
        # case 2: target < self.value
        if target < self.value:
            # if self.left is None, it isn't in tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # left side don't matter
        # iterate through nodes using a loop 
        # Only works for the test cases given
        if self.right is None:
            return self.value
        max_value = self.right.value
        while self.right is not None:
            if self.right.right is None:
                return self.right.value
            elif max_value < self.right.right.value:
                return self.right.right.value
            else:
                return max_value
        return max_value


        # Matt's recursive solution
        # if self.right is None:
        #     return self.value
        # return self.right.get_max()

        # Matt's iterative solution
        # if not self:
        #     return None
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        fn(self.value)
        if self.right is not None:
            # fn(self.right.value)
            self.right.for_each(fn)
        if self.left is not None:
            # fn(self.left.value)
            self.left.for_each(fn)

        # Matt's solution
        # fn(self.value)
        # if self.left:
            # self.left.for_each(fn)
        # if self.right:
            # self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if current node is none
            # we reached end of recursion, return
        if self is None:
            return
        # can we move left?
        if self.left is not None:
            self.left.in_order_print(node)

        # print current
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(node)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue to form a line for nodes
        queue = Queue()
        # start by placing root in queue
        queue.enqueue(self)
        # while loop, queue length greater than 0
        while len(queue) > 0:
            # dequeue item from front
            item = queue.dequeue()
            # print that item
            print(item.value)
            # place current item's left node in queue if not none
            if item.left is not None:
                queue.enqueue(item.left)
            # place current item's right node in queue if not none
            if item.right is not None:
                queue.enqueue(item.right
                )

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # inialize an empty stack
        stack = Stack()
        # push root node onto stack
        stack.push(node)
        # while loop, stack is not empty
        while len(stack) > 0:
            # pop top item off the stack
            item = stack.pop()
            # print item's value
            print(item.value)
            # if there is right subtree
            if item.right is not None:
                # push right item onto stack
                stack.push(item.right)
            # if there is a left subtree
            if item.left is not None:
                # push left item onto stack
                stack.push(item.left)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
