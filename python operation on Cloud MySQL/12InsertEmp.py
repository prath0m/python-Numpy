import pymysql

con=pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

no=int(input('Enter employee number : '))
nm=input('Enter name : ')
dp=input('Enter department : ')
po=input('Enter post : ')
sl=float(input('Enter salary : '))

try:
    curs.execute("insert into emp values(%d,'%s','%s','%s',%.2f)" %(no,nm,dp,po,sl))
    con.commit()
    print('new employee added successfully')
except:
    print('cant insert employee')


con.close()