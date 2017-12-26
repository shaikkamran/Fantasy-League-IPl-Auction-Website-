from databasecon import connection

def returntotalplayers():
	conn,c=connection()

	c.execute('select * from PlayersPrices')

	x=c.fetchall()
	return x
