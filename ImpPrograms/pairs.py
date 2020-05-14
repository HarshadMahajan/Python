def output(arr,ans):
    arr.sort()
    res=()
    list1=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==ans:
                res=(arr[i],arr[j])
                list1.append(res)
    print(list1)

def output1(arr,ans):
    res=()
    list1=[]
    while arr:
        num=arr.pop()
        diff=ans-num
        if diff in arr:
            list1.append((diff,num))
    print(list1)


arr=[1,3,5,4,2,7,10,6]
ans=7
res=output(arr,ans)
res=output1(arr,ans)
