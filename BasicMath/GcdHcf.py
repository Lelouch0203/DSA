gcd=1
n1=12
n2=24
# for i in range(min(n1,n2),0,-1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
#         break
# print(gcd)

while n1>0 and n2>0:
    if n1>n2:
        n1%=n2
    else:
        n2%=n1
    if n1==0:
        print(n2)
    else:
        print(n1)