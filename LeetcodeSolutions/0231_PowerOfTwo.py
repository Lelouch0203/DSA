def isPowerOfTwo(n):
    return n>0 and (n-1)&n==0
print(isPowerOfTwo(16))