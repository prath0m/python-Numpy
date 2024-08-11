import numpy

print('Creating numpy array from 2D List ')

lst=[
    [12,23,34],
    [54,56,78],
    [56,78,23],
    [45,78,90]
]

print(lst)

arr = numpy.array(lst)
print(arr)
print(arr.shape)