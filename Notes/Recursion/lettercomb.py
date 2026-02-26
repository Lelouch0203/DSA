# def keypad(s):
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
s = "23"
def bkt(strt,curr):
    if strt==len(s):
        res.append(curr)
        return 
    for i in range(0,len(mp[s[strt]])):
        bkt(strt+1,curr+mp[s[strt]][i])
bkt(0,"")
print(res)
