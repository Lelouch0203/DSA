def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
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
                if  (j in setj) or (i in seti):
                    matrix[i][j]=0
                    