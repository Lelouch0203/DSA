def generateParenthesis(n):
    def gen(open,close,n,curr,res):
        
        if len(curr)==n*2:
            res.append(curr)
            return 

        if open<n:
            gen(open+1,close,n,curr+'(',res)
        if close < open:
            gen(open,close+1,n,curr+')',res)
        
    res = []
    gen(0,0,n,"",res)
    return res
print(generateParenthesis(3))
        