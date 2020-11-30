class Node:  
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data,end=" ") 
            temp = temp.next
            
    def atBegining(self,newData):
        newNode=Node(newData)
        newNode.next = self.head
        self.head = newNode

    def atEnd(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=newNode

    def InBetween(self,prevData,newdata):
        if self.head.next is None:
            print("The mentioned node is absent")
            return
        temp = self.head
        curPos=self.head
        while (temp):
            if(temp.data==prevData):
                newNode = Node(newdata)
                newNode.next = curPos.next
                curPos.next=newNode
            temp=temp.next
            curPos=curPos.next
                
    def removeItem(self,removeData) :
        temp=self.head
        if(temp.data==removeData):
            temp=temp.next
            return
        while(temp):
            if(temp.data==removeData):
               break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next.next
        middle_node.next.next = NewNode

    def printNthItem(self,num):
        temp=self.head
        item=0
        while(temp != None):
            temp=temp.next
            item+=1
            if(item==num):
                print("\nThe {}rd item from the list is {}" .format(num, temp.data))

    def printNthItemrev(self,num):
        temp=self.head
        cnt=0
        while(temp != None):
            temp=temp.next
            cnt+=1
        temp = self.head
        for i in range(0,cnt-num):
            temp=temp.next
        print(temp.data)

    def pairwiseSwap(self): 
        temp = self.head 
        # There are no nodes in ilnked list 
        if temp is None: 
            return 
        # Traverse furthur only if there are at least two 
        # left 
        while(temp is not None and temp.next is not None): 
            # Swap data of node with its next node's data 
            temp.data, temp.next.data = temp.next.data, temp.data  
            # Move temo by 2 fro the next pair 
            temp = temp.next.next
           
        
list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Jan")

# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
e3.next = e4
#list1.printList()
list1.atBegining("Sun")
print("\n")
#list1.printList()
print("\n")
list1.atEnd("Sat")
#list1.printList()
print("\n")
list1.printList()
print("\n")
list1.Inbetween(list1.head.next,"Fri")
list1.printList()
print("\n")
list1.InBetween("Wed","Thurs")
list1.printList()
print("\n")
list1.removeItem("Wed")
list1.printList()
list1.printNthItem(3)
print("\n")
list1.printNthItemrev(5)
list1.printList()
print("\n")
list1.pairwiseSwap()
list1.printList()
