def median(nums1,nums2):
    if len(nums1)>len(nums2):
        return median(nums2,nums1)
    n1,n2=len(nums1),len(nums2)
    l,r=0,n1
    while l<=r:
        cut1=(l+r)//2
        cut2=(n1+n2+1)//2 - cut1
        
        l1=float('-inf') if cut1==0 else nums1[cut1-1]
        l2=float('-inf') if cut2==0 else nums2[cut2-1]
        
        r1=float('inf') if cut1==n1  else nums1[cut1]
        r2=float('inf') if cut2==n2  else nums2[cut2]
        
        
        if l1<=r2 and l2<=r1:
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        
            else:
                return  max(l1,l2)

        elif l1>r2 :
             r= cut1 - 1
        else:
            l=cut1+1
            
    return 0.0


a = [1, 3]
b = [2]
print("Median is:",median(a, b))
