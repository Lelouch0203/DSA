Sum=0
nums=[0,2,3,4]
N=len(nums)+1
actualsum=(len(nums)*(len(nums)+1))//2
for i in nums:
    Sum+=i
# print(actualsum-Sum) 


xor1 = 0
xor2 = 0

for i in range(N - 1):
    xor2 = xor2 ^ nums[i]  # XOR of array elements
    xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]

xor1 = xor1 ^ N  # XOR up to [1...N]
print(xor1 ^ xor2)  # the missing number
