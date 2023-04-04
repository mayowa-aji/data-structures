# FIFO - First in last out
# linked list is best for this when the front of the list is the first of the queue
 # -- We add new values to the end of the list and remove values from the front of the list. Think of it like a queue for food - the first person on the queue is served first and new customers join the end of the queue [Adding from the back and removing from the front]
# linked list and arrays work the same way for when the back of the list is the first of the queue

from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()

 # adding to the queue - no return because you are not calculating anything, just adding so you dont need a return
    def enqueue(self, value):
        self.data.add_back(value)

# taking something off the queue - when you delete you tend to return the value of the item you are deleting in case you want to do something with it later on.
    def dequeue(self, value):
        return self.data.delete_front()
