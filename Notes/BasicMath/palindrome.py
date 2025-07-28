def palindrome(n):
    asstr=str(n)
    for i in range(0,len(asstr)):
        if asstr[i]!=asstr[len(asstr)-i-1]:
            return False
    return True   
n=-121
# print(palindrome(n))

def isPalindrome(x):
    if x <0:
        return False
    n= str(x)
    n=n[::-1]
    if x == int(n):
        return True
    else:
        return False
print(isPalindrome(x=12321))