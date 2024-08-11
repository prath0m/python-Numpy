import numpy

file = open("cars.csv","r")

lst =[]

for car in file:
    try: 
        lst.append(int(car.split(',')[4]))
    except:
        pass

arr=numpy.array(lst)
# print(arr)    

print('Average KMS Car Driven is %.2f'%numpy.average(arr))

'''
swift,2014,4.6,6.87,42450,Diesel,Dealer,Manual,0

['swift','2014','4.6','6.87','42450','Diesel','Dealer','Manual','0']
'''