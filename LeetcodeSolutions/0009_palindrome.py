def isPalindrome(x):
    if x <0:
        return False
    n= str(x)
    n=n[::-1]
    if x == int(n):
        return True
    else:
        return False
x=121
print(isPalindrome(x))