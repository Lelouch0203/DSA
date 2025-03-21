from itertools import permutations
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans=[]

perm=list(permutations([x,y,z]))
for i in perm:
    if sum(i)!=n:
        ans.append(i)
print(ans)