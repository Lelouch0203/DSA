import time

start_time = time.time()
# Your code goes here
gcd=1
n1=999983
n2=999979
while n1>0 and n2>0:
    if n1>n2:
        n1%=n2
    else:
        n2%=n1
if n1==0:
    print(n2)
else:
    print(n1)
# Example:
for i in range(1000000):
    pass
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")







# gcd=1
# n1=999983
# n2=999979
# for i in range(min(n1,n2),0,-1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
#         break
# print(gcd)




