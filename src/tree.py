class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self,value):
        #helper function that takes a value and a root
        def helper(value, root):
         #start at the root
          curr_node = self.root
        #check to see if we found our value, if it does, then return true
          if curr_node.value == value:
             return True
          else:
            curr_value = curr_node.value
            if value < curr_value:
                self.helper(value, curr_node)
            else: # value > curr_value
               self.helper(value, curr_node)
        helper(value, self.root)


# if __name__ == '__main__':
#    tree = BinarySearchTree()
#    tree.root= Node(5)
#    tree.root.left= Node(3)
#    tree.root.right= Node(6)
#    tree.root.right.left= Node(1)
#    tree.root.right.right= Node(4)

#    print
