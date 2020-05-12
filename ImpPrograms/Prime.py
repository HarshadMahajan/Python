def primeNumber(num):
    isPrime =False
    if num > 0:
        for i in range(2,num):
            if(num%i != 0):
                isPrime = True
            else:
                isPrime =False
                break
    return isPrime

num = int(input("Enter the number"))
isPrime = primeNumber(num)
if(isPrime == True):
    print("Prime")
else:
    print("Not Prime")
