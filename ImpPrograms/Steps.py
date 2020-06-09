def staircase(n, X):
    cache = [0 for a in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

def staircase1(n, X):
    cache = [0 for a in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        a=0
        for x in X:
            if i - x >= 0:
                a+=cache[i - x]
        cache[i]+=a
    return cache[n]

def findStep(n,X):
    a=0
    if (n == 1 or n == 0) : 
        return 1
    elif (n == 2) : 
        return 2
    else :
        for x in X:
            a+=findStep(n - x)
    return a 
arr =staircase(4, [1,2,3])
arr1 =staircase1(4, [1,2,3])
arr2=findStep(4, [1,2,3])
print(arr)
print(arr1)
print(arr2)
