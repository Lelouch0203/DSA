# def gen(n,curr,result):
#     if len(curr)==n:
#         result.append(curr)
#         return
#     gen(n,curr+"0",result)
#     if not curr or curr[-1]!='1':
#         gen(n,curr+'1',result)
    
    
def gen(n,curr,result):
    if len(curr)==n:
        result.append(curr)
        return
    gen(n,curr+'0',result)
    if not curr or curr[-1]!='1':
        gen(n,curr+'1',result)
    
ans = []
gen(3,"",ans)
print(ans)