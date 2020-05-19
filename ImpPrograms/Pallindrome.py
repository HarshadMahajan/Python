def pallindrome(str1):
    start, end = 0, len(str1)-1
    while end > 0:
        if str1(start) == str1(end):
            return False
        else:
            return True
        start+=1
        end -=1

s='madam'
isPal = pallindrome(s)
print(isPal)
