import pymysql

conn = pymysql.connect(host='b35fhkxul9dakrrvpl8v-mysql.services.clever-cloud.com',user='ujdoqeqcusxjjas5',password='W5zppJbaAzak5mXKEMTO',database='b35fhkxul9dakrrvpl8v')
curs=con.cursor()

no=int(input('Enter account number : '))
curs.execute("select * from accounts where accno=%d" %no)
data=curs.fetchone()

if data:
    print(data)
    trans=input('Enter transaction (deposit/withdraw) : ')
    amt=float(input('Enter amount : '))

    if trans.lower()=='deposit':
        curs.execute("update accounts set balance=balance+%.2f where accno=%d" %(amt,no))
        con.commit()
        print('amount deposited successfully')
    elif trans.lower()=='withdraw':
        try:
            curs.execute("update accounts set balance=balance-%.2f where accno=%d" %(amt,no))
            con.commit()
            print('withdraw successful')
        except:
            print('insufficient balance')
    else:
        print('invalid transaction')
else:
    print('account does not exist')

con.close()