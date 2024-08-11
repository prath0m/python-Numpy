import numpy

lst=[
    [45,67],
    [67,89],
    [22,44]
]

arr = numpy.array(lst)


                #copying

a = arr             
print('arr ',arr)
print('a ',a)

print('ID of arr ',id(arr))
print('ID of a ',id(a))

arr +=3
print(arr)
print(a)

print('-'*45)

b = arr.view()
print(b)
print('ID of b ',id(b))


arr -=5
print(arr)
print(b)