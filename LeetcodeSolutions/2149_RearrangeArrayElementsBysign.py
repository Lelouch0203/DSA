
def rearrangeArray(nums):
    # p=[]
    # n=[]
    # for i in nums:
    #     if i>0:
    #         p.append(i)
    #     else:
    #         n.append(i)
    # i=0
    # j=0
    # k=0
    # while i < len(nums):
    #     if i %2==0:
    #         nums[i]=p[j]
    #         i+=1
    #         j+=1
    #     else:
    #         nums[i]=n[k]
    #         i+=1
    #         k+=1
    # return nums


    # posidx=0
    # negidx=1
    # ans=[0]*len(nums)
    # for i in nums:
    #     if i > 0:
    #         ans[posidx]=i
    #         posidx+=2
    #     else:
    #         ans[negidx]=i
    #         negidx+=2
    # return ans

    
    pos = []
    neg = []
    for n in nums:
        if n < 0:
            neg.append(n)
        else:
            pos.append(n)
    a = len(nums)
    nums[0:a:2] = pos
    nums[1:a:2] = neg
    return nums
