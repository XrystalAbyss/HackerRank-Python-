import numpy

arr = input().split()
arr = [int(i) for i in arr]
arr = numpy.array(arr)
arr = arr.reshape(3, 3)
print(arr)
