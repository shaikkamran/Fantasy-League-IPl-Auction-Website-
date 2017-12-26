from databasecon import connection
conn,c=connection()


def return1ifloggedIn(PlayerName):

	c.execute("select count(*) from Players where PlayerName=:PlayerName ",{"PlayerName":PlayerName})
	x=c.fetchall()
	
	if x[0][0]==1:

		return 1
	return 0

def returnfromPlayersbuyersreq(playername):
	c.execute('select b.TeamName,p.buyersprice from Buyers_ b '+
		',PlayersBuyersrequests_ p where p.playername=:playername and b.buyerid=p.buyerid  ',{"playername":playername})
	#print(c.fetchall())
	return (c.fetchall())

def returnPlayerDetailsBatsman(playername):
	c.execute('select * from BatsmanIpl where '
		+'Batsman_name=:playername',{"playername":playername})
	return (c.fetchall())
def returnPlayerDetailsBowlers(playername):
	c.execute('select * from BowlersIpl where '
		+'Bowlers_name=:playername',{"playername":playername})
	return (c.fetchall())

def playersTeamSelection(playername,playerteam):

	c.execute('update players set playerteam=:playerteam where playername=:playername',{"playerteam":playerteam,"playername":playername})
	conn.commit()
	c.execute("update bowlersipl set Bowlers_team=:playerteam where Bowlers_name=:playername",{"playerteam":playerteam,"playername":playername})
	conn.commit()
	c.execute("update batsmanipl set Batsman_team=:playerteam where batsman_name=:playername",{"playerteam":playerteam,"playername":playername})
	conn.commit()
	c.execute('delete from playerprices where playername=:playername',{"playername":playername})
	conn.commit()
	c.execute('delete from playersbuyersrequests_ where playername=:playername',{"playername":playername})
	conn.commit()

#print(returnPlayerDetailsBatsman('AB de Villiers'))
#print(returnPlayerDetailsBowlers('Virat Kohli'))

