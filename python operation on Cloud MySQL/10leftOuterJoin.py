import pymysql

con = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')

curs = con.cursor()

curs.execute("select customers.custnm, products.prodnm, products.company, products.price from customers left outer join products on customers.prodid= products.prodid")

data = curs.fetchall()

print(data)

con.close()
