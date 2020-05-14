def decToBin(num):
    i=0
    arr=[]
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else:
        while num > 0:
            rem = num%2
            arr.append(rem)
            num=num//2
            i+=1
    print(arr)
    print(i)
    for j in range(i-1,-1,-1):
        print(arr[j],end="")

decToBin(19)
