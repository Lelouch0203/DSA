def ispalindrome(num):
    # return str(num)==str(num)[::-1]
    if num < 0 :
        return False
    num=str(num)
    for i in  range(len(num)//2):
        if num[i]!=num[len(num)-1-i]:
            return False
    return True

# print(ispalindrome(12621))


def fib(n):
    if n == 0 :
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

# print(fib(7))



def freqOfMostfreq(arr,k):
    arr.sort()
    left=0
    sumofwin=0
    maxlenofwin=0
    for right in range(len(arr)):
        sumofwin+=arr[right]
        # lenOfWin=right-left+1
        target=arr[right]
        while ((right-left+1)*target)-sumofwin>k:
            sumofwin-=arr[left]
            left+=1
        maxlenofwin=max(right-left+1,maxlenofwin)
    return maxlenofwin
        
# print(freqOfMostfreq([3,4,5,12,19,22,44,150],32))



def arraySortedRotated(arr):
    if arr == sorted(arr):
        return True
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            return arr[i+1:]+arr[:i+1]==sorted(arr)

# print(arraySortedRotated([3,4,5,1,2]))


def moveZeros(arr):
    nonz=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[nonz]=arr[nonz],arr[i]
            nonz+=1
    return arr
            
# print(moveZeros([ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
def missingNr(arr):
    xor1=0
    xor2=0
    for i in range(len(arr)):
        xor1^=arr[i]
        xor2^=i+1
    xor2^=len(arr)+1
    return xor2 ^ xor1

print(missingNr([1,2,3,4,6,7]))
        
            
            
    



