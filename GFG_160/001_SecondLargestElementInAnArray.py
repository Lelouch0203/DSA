def getSecondLargest(self, arr):
    sortedset = sorted(set(arr))
    if (len(sortedset)== 1 or 0):
        return -1
    else:
        return sortedset[-2]    
    
if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],
        [10, 10, 10],
        [5, 1, 5, 2],
        [7],
        [8, 6, 8, 4, 6, 2]
    ]
    for arr in test_arrays:
        result = getSecondLargest(None, arr)
        print(f"Array: {arr} -> Second Largest: {result}")