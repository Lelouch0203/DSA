import time
strttime=time.time()
matrix =[[1,1,1],
         [1,0,1],
         [1,1,1]]
m=len(matrix)
n=len(matrix[0])
seti=set()
setj=set()
for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            seti.add(i)
            setj.add(j)
for i in range(m):
    for j in range(n):
        if i in seti or j in setj:
            matrix[i][j] = 0

print(matrix)
endtime=time.time()
print(endtime-strttime)