class Stack:
    stackArray=[]
    def __init__(self,no):
        self.no=no

    def insertNumber(self):
        Stack.stackArray.append(self.no)

    def deleteNumber(self):
        if len(Stack.stackArray) >0:
            Stack.stackArray.pop()
        else:
            print("No element in Stack to Delete")
            

    def printArray(self):
        print(Stack.stackArray)

while True:
    print ('===Menu===')
    print ('1. Insert')
    print ('2. Delete')
    print ('3. Print')
    print ('4. Exit')
    try:
        choice=int(input('Enter a choice: '))
        num=0
        if choice==1:
            num=int(input("Enter a number :"))
            objStock = Stack(num)
            objStock.insertNumber()
            continue
        elif choice==2:
            objStock = Stack(num)
            objStock.deleteNumber()
            continue
        elif choice==3:
            objStock = Stack(num)
            objStock.printArray()
            continue
        else:
            print( "Invalid Input" )
    except ValueError:
        pass
        
