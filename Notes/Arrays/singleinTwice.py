nums=[3,3,2,1,1]


x=0
for i in nums:
    x=x^i
print(x)

m={}
# for i in nums:
#     m[i]=m.get(i,0)+1
# for num,count in m.items():
#     if count==1:
#         print(num)
#         break