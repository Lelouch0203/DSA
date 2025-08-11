def checkPalindrome(s,n,i):
    if i>=n/2:
        return True
    return s[i]==s[n-i-1] and checkPalindrome(s,n,i+1)
print(checkPalindrome("werrw",5,0))

strr="jaisai"
print([strr[::-1]])