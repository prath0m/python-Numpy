import numpy
import pymysql

con=pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

curs.execute("select * from accounts")
data= curs.fetchall()

arr= numpy.array(data)
print(arr)
print(arr.shape)
con.close()
