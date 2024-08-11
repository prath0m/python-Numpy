import numpy

arr = numpy.random.random(9)
print(arr)

arr= numpy.random.random((3,4))
print(arr)

arr = numpy.random.randint(1,35,9)
print(arr)

lst= [12,23,34,56,67,78,89,90]
arr = numpy.array(lst)
x=numpy.random.choice(arr)
print(x)

print(arr)
numpy.random.shuffle(arr)
print(arr)