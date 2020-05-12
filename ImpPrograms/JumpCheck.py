def checkJump(list2):
    list3=[]
    jump=0
    for i in range(0,len(list2)):
        if list2[i]==0:
            list3.append(i)
    print(list3)
    for j in range(0,len(list3)-1):
        if list3[j+1]-list3[j]==1:
            print("here")
            pass
        else:
            print("there")
            jump+=1
        
    return jump


list1=[]
ip=int(input("How many numbers"))
'''for i in range(ip):
    val=int(input("Enter the value"))
    list1.append(val)'''
list1=[0,1,0,0,0,1,0]


output=checkJump(list1)
print(output)
