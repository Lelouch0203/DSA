def hammingWeight(self, n: int) -> int:
    # cnt = 0 
    # while n :
    #     n = n & (n-1)
    #     cnt+=1
    # return cnt
    return n.bit_count()
print(hammingWeight(0,11))
