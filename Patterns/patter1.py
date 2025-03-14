n = 5
for i in range(0,n):
    for j in range(n):
        print("*",end=" ")
    print()
    
print()

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

print()

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
print()

for i in range(0,n):
    for j in range(0,n-i):
           print("*",end=" ")
    print()
    
print()

for i in range(0,n):
    for j in range(1,n-i+1):
           print(j,end=" ")
    print()
    
print()

for i in range(0,n):    
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    for j in range(0,i):
        print("*",end="")
    print()

print()

for i in range(0,n):
    for j in range(0,i):
        print("",end=' ')
    for j in range(0,11-(2*(i+1))):
        print("*",end='')
    for j in range(0,i):
        print("",end=' ')
    print()
    
print()

for i in range(0,n):    
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(0,n):
    for j in range(0,i):
        print("",end=' ')
    for j in range(0,11-(2*(i+1))):
        print("*",end='')
    for j in range(0,i):
        print("",end=' ')
    print()
    
print()

for i in range(0,2*n-1):
    if i>4:
        for j in range(0,2*n-(i+1)):
            print("*",end=" ")
    else:
        for j in range(0,i+1):
            print("*",end=" ")
    
    print()
    
print()

for i in range(0,n):
    for j in range(0,i+1):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()

print()

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     for j in range(0,2*(n-i)):
        