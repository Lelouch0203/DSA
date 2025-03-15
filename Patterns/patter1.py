
# 1
n = 5
for i in range(0, n):
    for j in range(n):
        print("*", end=" ")
    print()

print()

# 2
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

print()

# 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print()

# 5
for i in range(0, n):
    for j in range(0, n - i):
        print("*", end=" ")
    print()

print()

# 6
for i in range(0, n):
    for j in range(1, n - i + 1):
        print(j, end=" ")
    print()

print()

# 7
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    for j in range(0, i):
        print("*", end="")
    print()

print()

# 8
for i in range(0, n):
    for j in range(0, i):
        print("", end=' ')
    for j in range(0, 11 - (2 * (i + 1))):
        print("*", end='')
    for j in range(0, i):
        print("", end=' ')
    print()

print()

# 9
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(0, n):
    for j in range(0, i):
        print("", end=' ')
    for j in range(0, 11 - (2 * (i + 1))):
        print("*", end='')
    for j in range(0, i):
        print("", end=' ')
    print()

print()

# 10
for i in range(0, 2 * n - 1):
    if i > 4:
        for j in range(0, 2 * n - (i + 1)):
            print("*", end=" ")
    else:
        for j in range(0, i + 1):
            print("*", end=" ")
    print()

print()

# 11
for i in range(0, n):
    for j in range(0, i + 1):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

print()

# 12
for i in range(0, n):
    for j in range(0, i + 1):
        print(j + 1, end="")
    for j in range(0, 2 * (n - i - 1)):
        print(" ", end="")
    for j in range(i + 1, 0, -1):
        print(j, end="")
    print()

print()

# 13
num = ord('A')
for i in range(0, n):
    for j in range(0, i + 1):
        print(chr(num + j), end=" ")
    print()

print()

# 14
for i in range(0, n):
    for j in range(0, n - i):
        print(chr(num + j), end=" ")
    print()

print()

# 15
for i in range(0, n):
    for j in range(0, i + 1):
        print(chr(num + i), end=" ")
    print()

print()

# 16
for i in range(0, n):
    for j in range(0, n - i):
        print(chr(num + i), end=" ")
    print()

print()

# 17
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print(chr(num + j), end='')
    for j in range(i,0,-1):
        print(chr(num + j-1), end='')
    print()
print()

# 18
newNUm=ord('E')
for i in range(0, n):
    for j in range(i+1,0,-1):
        print(chr(newNUm-j+1), end=" ")
    print()

print()

# 19
for i in range(0,n):

    for j in range(0,n-i):
        print("*",end=" ")
    for j in range(0,2*i):
        print(" ",end=" ")
    for j in range(0,n-i):
        print("*",end=" ")
    print()
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,2*(n-i-1)):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
    
print()

#20
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,2*(n-i-1)):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(0,n):
    for j in range(0,n-i-1):
        print("*",end=" ")
    for j in range(0,2*(i+1)):
        print(" ",end=" ")
    for j in range(0,n-i-1):
        print("*",end=" ")
    print()
    
print()

# 21
for i in range(0,n):
    for j in range(0,n):
        if i==0 or j==0 or i == n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

# 22
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        top = i
        left = j
        right=(2*n-2)-j
        bottom= (2*n-2)-i
        print(n-min(top,bottom,right,left),end=" ")
    print()