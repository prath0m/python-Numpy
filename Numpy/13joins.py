import numpy
# Joining

a1 = numpy.array([34,45])
a2 = numpy.array([45,67,78,90,89])

a3 = numpy.concatenate((a1,a2))
print(a3)

a1 = numpy.array([[21,34,34],[45,56,67]])
a2 = numpy.array([[6,7,8],[8,9,0],[12,23,43]])

a3 = numpy.concatenate((a1,a2))
print(a3)


print('-'*45)

a1 = numpy.array([[1,2,3],[4,5,6]])
a2 = numpy.array([[7,8],[9,0]])

a3 = numpy.concatenate((a1,a2),axis=1)
print(a3)

