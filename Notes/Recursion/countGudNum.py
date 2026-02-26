def cnt(n):
    mod = 10**9+7
    def pow(x,y,mod):
        if y==0:
            return 1
        half = pow(x,y//2,mod)  
        half = (half*half)%mod
        
        if y%2==1:
            half = (half*x)%mod     
        return half 
    o = n//2
    e = (n+1)//2
    return pow(5,e,mod)*pow(4,o,mod)%mod
print(cnt(4))