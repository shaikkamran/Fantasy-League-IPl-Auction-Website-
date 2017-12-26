from collections import defaultdict

dc=defaultdict(list)

def returnlists(user,newval1,newval2):
	global dc
	l=0
	if user in dc:
		for i in dc[user]:
			if i[1]==newval1:
				i[3]=newval2
				l=1
	if l==0:			
		dc[user].append([int(user),newval1,'',newval2])
	print(dc)	
	return dc	
def returndc(user):
	global dc
	m=defaultdict(list)
	for i in dc:
		if i!=user:
			m[i]=dc[i]
			
	return m		


	

def returnlist(user):
	global dc
	if user in dc:
		return dc[user]
	return []	
def deletedc(user):
	global dc
	if user in dc:
		del dc[user]
	return []	

