class Node:
     def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # to keep track of the nodes
        self.head = None
        self.tail = None

    def add_front(self, value):
        if self.head is None:  # our list is empty (which means that the node is both the head and the tail)
          new_node = Node(value)
          new_node.next = self.head
          self.head = new_node
          self.tail = new_node
        else: # our list is not empty so we know it is the head
          new_node = Node(value)
          new_node.next = self.head
          self.head = new_node

    def add_back(self, value):
        new_node = Node(value)
        if self.head is None:
          self.add_front(value)
        # calling the add front method because already have the logic to check if it is head or tail
        else:
          self.tail.next = new_node
          self.tail = new_node

    def delete_front(self):
       #checking if link is not empty
      if self.head is not None:
          # if not empty
          self.head = self.head.next
          # checks to see if there is only one link(i.e. a head and a tail)
      elif self.head.next is None:
          self.head = None
          self.tail = None

    def delete_back(self):
        curr_node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while curr_node.next is not self.tail:
                curr_node = curr_node.next
                # once we find the tail node, assign the new tail to the current node
                self.tail = curr_node
                self.tail.next = None

            curr_node.next = None








