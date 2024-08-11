import pymysql

con=pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

no=int(input('Enter account number : '))
nm=input('Enter account name : ')
ty=input('Enter account type : ')
bal=float(input('Enter balance : '))

# insert into accounts values(1052,'praffull','current',139000)
curs.execute("insert into accounts values(%d,'%s','%s',%.2f)" %(no,nm,ty,bal))
con.commit()
print('new account opened successfully')

con.close()