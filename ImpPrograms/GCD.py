import math

def gcdforList(a, b):
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    result = a[0]
    for i in a[1:]:
        result = gcd(result, i)
    return result

a = [4, 10, 16, 14]
b =4
c = gcdforList(a,b)
print(c)

print(int(math.floor(20.75+(20.75*10/100)+(20.75*3/100))))


list1 =[["Ajay",12.5],["Vijay",35.5],["Sanjay",70]]
for x in list1:
    print(x[1])
