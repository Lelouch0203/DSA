import heapq
def sortbyfreq(s):
    count={}
    for char in s:
        count[char]=count.get(char,0)+1
    heap=[]
    for char in s :
        heapq.heappush(heap,(count[char],char))
    print(count)
    print(heap)
    res=""
    for     i in heap:
        res+=(heapq.heappop(heap)[1])
    return res
print(sortbyfreq("tree"))