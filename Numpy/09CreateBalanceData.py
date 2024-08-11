# Only one column to show in the numpy array

import numpy
import pymysql

con=pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

curs.execute("select balance from accounts")
data= curs.fetchall()
con.close()

#arr = numpy.array(data)

lst =[]  #create empty list

for rec in data:
    lst.append(rec[0])   #put all the specific column data into list

arr = numpy.array(lst)  #create numpy array

print(arr)