from databasecon import connection

conn,c=connection()

c.execute('select * from PlayersPrices_')
x=c.fetchall()
for i in x :
	print(i);break;