def poset(s,index,current,result):
    if index == len(s):
        if current:
            result.append(current)
        return result
    poset(s,index+1,current,result)
    poset(s,index+1,current+s[index],result)
    return result
    
print(poset('abc',0,'',[]))
