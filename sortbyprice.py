from databasecon import connection
conn,c=connection()

def returnpricehightolow():
	c.execute('select * from PlayerPrices order by playerPrice desc')
	return c.fetchall()


def returnpricelowtohigh():
	c.execute('select * from PlayerPrices order by playerPrice ')
	return c.fetchall()
	
def returnOrderByNameAsc():
	c.execute('select * from PlayerPrices order by playername  ')
	return c.fetchall()
def returnOrderByNameDesc():
	c.execute('select * from PlayerPrices order by playername desc ')
	return c.fetchall()
	
