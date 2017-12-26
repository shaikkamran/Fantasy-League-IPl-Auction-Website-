from databasecon import connection
conn,c=connection()


def return1ifloggedin(buyerid,password):

	c.execute("select count(*) from Buyers_ where Buyerid=:buyerid and password=:password" ,{"buyerid":buyerid,"password":password})
	x=c.fetchall()
	
	if x[0][0]==1:

		return 1
	return 0	
	
def insertintoPlayersBuyersRequests(lis):
	
	for i in lis:
		buyerid=i[0]
		buyersprice=i[3]
		playername=i[1]
		c.execute("select count(*) from PlayersBuyersrequests_ where Buyerid=:buyerid and PlayerName=:playername" ,{"buyerid":buyerid,"playername":playername})
		x=c.fetchall()
		if x[0][0]==0:
			#print('snjd')
			c.execute('insert into PlayersBuyersrequests_ values (?,?,?,?)',i)			
			

		else:# x==0:
			#print('shdj')
			c.execute("update Playersbuyersrequests_ set Buyersprice=:buyersprice where Playername=:playername and buyerid=:buyerid  ",{"buyerid":buyerid,"playername":playername,"buyersprice":buyersprice})
			
			
		conn.commit()	
	#c.execute('select * from PlayersBuyersrequests_')
	#print(c.fetchall())		
		
		#print(i[0])
#insertintoPlayersBuyersRequests([[1001,'AB de Villiers','',90090]])
#insertintoPlayersBuyersRequests([[1002,'Virat Kohli','',9]])
