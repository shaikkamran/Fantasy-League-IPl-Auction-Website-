from databasecon  import connection
import numpy as np
import csv

def typecast(col_list,arr,st):
	for i in col_list:
	
		for j in range (len(arr)):
			if st=='i':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=int(arr[j][i])
				else:
					arr[j][i]=None
			elif st=='f':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=float(arr[j][i])
				else:
					arr[j][i]=None	
				
			#print(arr[0][j])
	return arr		


final=m=[ ['' for i in range(15)]for j in range (159)]
k=[]
l=[]
conn,c=connection()
with open('batsmanipl2016.csv') as csv_file:
	csvreader=csv.reader(csv_file)
	#print(csvreader)
	next(csvreader)
	cm=0;x=0
	for line in csvreader:
		print(line)
		if line !=['Pos', 'Player', 'Mat', 'Inns', 'NO', 'Runs', 'HS', 'Avg', 'BF', 'SR', '100', '50', '4s', '6s'] :
			if line[0]!='':
				l.append(line)
				cm+=1
			else:
				k.append(line[1])
				x+=1
	#print(c,x)
print(len(l),len(k),len(l[0]))			
for i in range (len(k)):
	for j in range (len(l[0])):
		m[i][j]=l[i][j]
	m[i][14]=k[i]					
#print(m[0][1])
m=typecast([0,2,3,4,5,8,10,11,12,13],m,'i')
m=typecast([7,9],m,'f')

#c.executemany('insert into BatsmanIpl values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',m)


conn.commit()

conn.close()
