from databasecon  import connection
import numpy as np
import csv




conn,c=connection()
def scrapefromcsv(filenames):
    k=[]
    l=[]
    
    with open(filenames) as csv_file:
            csvreader=csv.reader(csv_file)
            #print(csvreader)
            next(csvreader)
            cm=0;x=0
            for line in csvreader:
                    #print(line[0])
                    if line[0] !='Pos':#, 'Player', 'Mat', 'Inns', 'NO', 'Runs', 'HS', 'Avg', 'BF', 'SR', '100', '50', '4s', '6s'] :
                            if line[0]!='':
                                    l.append(line)
                                    cm+=1
                            else:
                                    k.append(line[1])
                                    x+=1
    #print(c,x)
    m=[['' for i in range(len(l[0])+1)]for j in range (len(l))]                           
    for i in range (len(k)):
            for j in range (len(l[0])):
                    m[i][j]=l[i][j]
            m[i][len(l[0])]=k[i]
    m=np.array(m)
    a=m[:,1][:,None]
    b=m[:,len(l[0])][:,None]
    o=np.hstack((a,b))    
    return o                                
#print(len(l),len(k))
files=['bowlersipl2016.csv','batsmanipl2016.csv']
x=np.vstack(scrapefromcsv(files[0]))
y=np.vstack(scrapefromcsv(files[1]))

'''for i in files:
    
    x=np.vstack(scrapefromcsv(i))
    print('end')'''


