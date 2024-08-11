import pymysql
conn = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs= conn.cursor()
typ = input("Enter Account Type: ")
curs.execute("Select * from accounts where acctype = '%s'"%typ)
data = curs.fetchall()
print(data)
conn.close()