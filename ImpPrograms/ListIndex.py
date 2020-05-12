def checkIndex(list2):
    list1=[]
    for i in range(0,len(list2)):
        if i==list2[i]:
            print("Here")
            list1.append(i)
    return list1

list2 =[-3,-5,3,2,4,5]
output=checkIndex(list2)
if len(output) >= 1:
    output.sort()
    print("The matching lowest index and element is : " + str(output[0]))
else:
    print("None")
