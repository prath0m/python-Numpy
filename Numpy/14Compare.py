import numpy

a1 = numpy.array([[1,2,3],[4,5,6]])
a2 = numpy.array([[1,2,9],[4,8,7]])

comp = (a1==a2)
print(comp)
print(comp.all())