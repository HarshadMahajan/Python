def checkValley(steps,path):
    altitude=0
    valley=0
    list1 = list(path)
    for slop in list1:
        if slop == 'D':
            altitude-=1
        if slop == 'U':
            altitude+=1
            if altitude==0:
                valley+=1
    return valley


list1=[]
steps=int(input("How many steps"))
path=input("Enter the path")
output=checkValley(steps,path)
print(output)
