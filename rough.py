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

# print(missingNr([1,2,3,4,6,7]))
        
            
# intervals=[[1,3],[1,4],[2,5],[3,5]]
# numbers = sorted(set(num for start, end in intervals for num in range(start, end + 1)))
# count=[-2]*len(intervals)
# for num in numbers:
#     for j in range(len(intervals)):
#         if intervals[j][0]<=num and num<=intervals[j][1]:
            
#             count[j]+=1
#             print(count)
# summ  = sum(count)
# if summ>len(numbers):
#     print(len(numbers)-summ%len(intervals))
# else:
#     print(len(numbers)-summ)
            
# nums=[0,1,2,2,3,0,4,2]
# val =2            
# i = 0
# j = 0
# cnt=0
# while j<len(nums):
#     if nums[j]!=val:
#         nums[i],nums[j] = nums[j],nums[i]
#         i+=1
#         j+=1
#     else:
#         cnt+=1
#         j+=1
# print(nums,cnt)

# def get_3x3_matrices(grid):
#     matrices = []
#     rows = len(grid)
#     cols = len(grid[0])
    
#     for i in range(rows - 2):
#         for j in range(cols - 2):
#             mat = [grid[i+k][j:j+3] for k in range(3)]
#             matrices.append(mat)
    
#     return matrices
# grid = [[4,3,8,4,2],[9,5,1,9,3],[2,7,6,2,3]]
# print(get_3x3_matrices(grid))

