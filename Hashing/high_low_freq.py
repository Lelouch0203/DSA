def freqcalc(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    maxfreq=0
    minfreq=len(arr)
    max=0
    min=0
    
    for i in mp:
        
        if mp[i]>maxfreq:
            maxfreq=mp[i]
            max=i
        if mp[i]<minfreq:
            minfreq=mp[i]
            min=i
    print(max,min)
freqcalc(arr = [10,5,10,15,10,5])