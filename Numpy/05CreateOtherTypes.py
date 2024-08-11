import numpy

print("creating numpy array of datatypes: ")

arr = numpy.array(['skoda','toyota','maruti','BMW','honda'])
print(arr)

arr = numpy.arange('2023-07-28','2023-08-31',dtype="datetime64[D]")
print(arr)

arr= numpy.array([True,False,False,True,False,True])
print(arr)