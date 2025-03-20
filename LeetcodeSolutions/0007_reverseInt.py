def reverse(self, x):
    revNum = 0
    is_negative = x < 0 
    x = abs(x)  

    while x != 0:
        digit = x % 10 
        revNum = revNum * 10 + digit  
        x //= 10  


    if is_negative:
        revNum = -revNum


    if revNum < -2**31 or revNum > 2**31 - 1:
        return 0

    return revNum
x=123
print(reverse(0,x))