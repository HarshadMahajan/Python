from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        self.head == None
    
    # O(1)
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # O(n)
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
    
    # O(n)
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    # O(n)
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:               
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    # O(n), we can make it O(1)
    def append(self, item):
        """add items into the last linked list, reverse from add"""
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(None)
        current.setNext(temp)
    
    # O(n)
    def insert(self, item, index):
        """insert item after certain index (start with 0)"""
        current = self.head
        if index > self.size() - 1:
            raise("index out of range")

        for i in range(index):
            current = current.getNext()
        
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)
    
    # O(n)
    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(None)
            

    
            
        
    