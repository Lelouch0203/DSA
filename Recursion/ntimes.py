# def print_numbers(n):
#     if n <= 0:
#         return
#     print_numbers(n - 1)
#     print(n,end=' ')

# # Example usage
# n = 5
# print_numbers(n)
def pushZerosToEnd(arr):
    count = 0
    ans=[]
    for i in arr:
        if i==0:
            count+=1
        else:
            ans.append(i)
    for i in range(count):
        ans.append(0)
    return ans        
pushZerosToEnd([3 ,5 ,0 ,0, 4])