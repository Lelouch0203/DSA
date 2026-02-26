def letterCombinations( digits) :
    mp = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
    }
    res = []
    def btk(strt,curr):
        if strt == len(digits):
            res.append(curr)
            return 
        for i in range(0,len(mp[digits[strt]])):
            btk(strt+1,curr+mp[digits[strt]][i])
    btk(0,"")
    return res
print(letterCombinations("23"))