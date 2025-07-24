# x=1
# y=1
# z=2
# coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
# print(coordinates)

import numpy
n=7
meetings=[[2,4],[1,3]]   

meetings=sorted(meetings)
new=(numpy.array(meetings).flatten())
print(sorted([int (x) for x in new]))