import numpy
n,m=map(int,input().split())
array=numpy.array([input().strip().split() for array in range(n)],int)
print(numpy.transpose(array))
print(array.flatten())
