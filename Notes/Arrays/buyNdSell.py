arr = [7, 1, 5, 3, 6, 4]
maxpro=0
minPrice=float('inf')
for i in range(len(arr)):
    minPrice=min(minPrice,arr[i])
    maxpro=max(maxpro,arr[i]-minPrice)
    
    
print (maxpro)