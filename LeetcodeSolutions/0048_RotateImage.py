matrix=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
for i in range(n//2):
    matrix[i],matrix[n-i-1]=matrix[n-i-1],matrix[i]

for i in range(n):
    for j in range(n):
        if i<j:
         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print(matrix)

        