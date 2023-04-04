#LIFO Last in, first out

class Stack:
    def __init__(self):
        #back of the list is top of the stack so use an array instead of a linked list as it is more efficient
        self.data = []

    #to add things to the top of the stack
    def push(self, value):
        self.data.append(value)

    #remove things from the top of the stack
    def pop(self):
        return self.data.pop()

if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('b')
    print (s.data)
    s.pop()
    print (s.data)

