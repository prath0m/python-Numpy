import pymysql
conn = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs = conn.cursor()
no = int(input('Enter Employee number: '))

curs.execute("Select * from emp where empno=%d" %no)
data = curs.fetchone()
try:
    print('Name: ',data[1])
    print('Post: ',data[3])
    print('Salary: ',data[4])
except:
    print('employee number not found')
conn.close()