import pymysql

con=pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

no=int(input('Enter employee number : '))
curs.execute("select * from emp where empno=%d" %no)
data=curs.fetchone()
if data:
    print(data)
    sl=float(input('Enter new salary : '))
    curs.execute("update emp set salary=%.2f where empno=%d" %(sl,no))
    con.commit()
    print('salary updated successfully')
else:
    print('employee number not found')

con.close()
