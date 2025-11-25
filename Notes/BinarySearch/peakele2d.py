def peak2d(mat):
    m=len(mat)
    n=len(mat[0])
    l=1
    r=m*n-2
    while l<=r:
        mid=(l+r)//2
        row=mid//n
        col=mid%n
        middle = mat[row][col]
        