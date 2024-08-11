# create numpy array from from python list

import numpy

print('create numpy array from from python list')

lst1 = [12,23,34,45,56,67,78,89,90]
print(lst1)
print(type(lst1))

arr=numpy.array(lst1)
print(arr)

arr = arr ** 2
print(arr)
