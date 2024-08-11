import pymysql

conn = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

no=int(input('Enter account number : '))
#select * from accounts where accno=1032

curs.execute("select * from accounts where accno=%d" %no)
data=curs.fetchone()
print(data)

con.close()



