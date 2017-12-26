from flask import Flask, render_template,flash,url_for,request,redirect,session,abort,g
from wtforms import Form,validators,StringField,PasswordField
from Playerprices import returntotalplayers
from sortbyprice import returnpricehightolow,returnpricelowtohigh,returnOrderByNameAsc,returnOrderByNameDesc
from checkbuyerslogin import return1ifloggedin,insertintoPlayersBuyersRequests
from databasecon import connection
from checkplayerslogin import return1ifloggedIn,returnPlayerDetailsBatsman,returnPlayerDetailsBowlers,returnfromPlayersbuyersreq,playersTeamSelection

from retlist import returnlists,returnlist,deletedc,returndc
conn,c=connection()

import os
app = Flask(__name__)




def returnlogoutfbcciloggedin():
	if 'user' in session:
		if session['user']=='admin':
			session.pop('user',None)

def returnifbuyerloggedin():
	if 'user' in session:
		if return1ifloggedin(session['user'],session['user'])==1:
	
			session.pop('user',None)

def returnifplayerloggedin():
	if 'user' in session:
		if return1ifloggedIn(session['user'])==1:
	
			session.pop('user',None)




@app.before_request
def before_request():
	g.user=None
	
	if 'user' in session:
		g.user=session['user']	

@app.route('/bccilogin')
def bcciportal():
	
	returnifbuyerloggedin()
	returnifplayerloggedin()

	if 'user'  not in session:
		return render_template('bccilogin.html')
		
	else:
		return 'logged into bcci as  '+str(g.user)
	

	
@app.route('/bcciportal',methods=['POST'])
def bccigologin():
	
	if request.form['password'] == 'pwd' and request.form['username'] == 'admin':
		session['user'] = 'admin'
		
	
		
	return redirect(url_for('bcciportal'))


@app.route('/')
def hello_name():
   return render_template('newhome.html')



@app.route('/buyersportal')

def buyersportal():
	
	returnlogoutfbcciloggedin()
	returnifplayerloggedin()
	if  'user' not in session:
	
		return render_template('Buyerslogin.html')
	else :
		

		return   redirect(url_for('buyerspot',message='pricebyhightolow',lis=returnlist(session['user']),otherslis=returndc(session['user'])))			

   
@app.route('/blogin',methods=['POST'])
def buyersgologin():
	buyerid=request.form['username']
	flag=return1ifloggedin(buyerid,request.form['password'])

	if flag==1:
		session['user'] = buyerid
		
	return redirect(url_for('buyersportal'))
	
@app.route('/logout')
def logout():
	session.pop('user',None)
	return redirect(url_for('hello_name'))

@app.route('/buyersportal/<message>',methods=['get','post'])

def buyerspot(message):
	returnlogoutfbcciloggedin()

	if 'user' in session:
	
		if message=='pricebyhightolow':	
			
			return render_template('players1new.html',PlayerPrices=returnpricehightolow(),lis=returnlist(session['user']),otherslis=returndc(session['user']))	
		elif message=='pricebylowtohigh':
			return render_template('players1new.html',PlayerPrices=returnpricelowtohigh(),lis=returnlist(session['user']),otherslis=returndc(session['user']))
		elif message=='sortbyplayernameasc':
			return render_template('players1new.html',PlayerPrices=returnOrderByNameAsc(),lis=returnlist(session['user']),otherslis=returndc(session['user']))
		elif message=='sortbyplayernamedesc':
			return render_template('players1new.html',PlayerPrices=returnOrderByNameDesc(),lis=returnlist(session['user']),otherslis=returndc(session['user']))
		
		
	else:
		return redirect(url_for('buyersportal'))



@app.route('/buyersportal/allplayers',methods=['get','post'])
def buyersrequests():
	returnlogoutfbcciloggedin()
	returnifplayerloggedin()

	if 'user' in session :
		x = request.form['pn']
		dc=returnlists(session['user'],request.form['pn'],request.form['price'])
		
		return redirect(url_for('buyerspot',message='pricebyhightolow',lis=returnlist(session['user']),otherslis=returndc(session['user'])))		
	else:
		return redirect(url_for('buyersportal'))


@app.route('/buyersportal/allplayersrequests',methods=['get','post'])
def buyersrequeststodb():
	returnlogoutfbcciloggedin()
	returnifplayerloggedin()				
	
	if 'user' in session:
		
		insertintoPlayersBuyersRequests(returnlist(session['user']))
		
		
		
		return redirect(url_for('buyerspot',message='pricebyhightolow',lis=deletedc(session['user']),otherslis=returndc(session['user'])))		
	else:
		return redirect(url_for('buyersportal'))




@app.errorhandler(400)
def page_not_found(e):
	return render_template('404_not_found.html')	 


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404_not_found.html')	 
@app.errorhandler(405)
def method_not_found(e):
	return render_template('405_not_found.html')	 




@app.route('/playerslogin')
def playerportal():
	returnlogoutfbcciloggedin()
	returnifbuyerloggedin()

	if  'user' not in session :
	

		return render_template('playerslogin.html')
	else :

		BatsmanAcievements=returnPlayerDetailsBatsman(session['user'])
		BowlersAcievements=returnPlayerDetailsBowlers(session['user'])
		buyersdetails=returnfromPlayersbuyersreq(session['user'])

		return   render_template('Players.html',playername=session['user'],buyersdetails=buyersdetails,BatsmanAcievements=BatsmanAcievements,BowlersAcievements=BowlersAcievements)

@app.route('/player',methods=['POST'])
def player():
	
	if return1ifloggedIn(request.form['username'])==1 :
		session['user'] = request.form['username']
	return redirect(url_for('playerportal'))

@app.route('/playerschoice',methods=['POST'])
def playerschoice():
	
	if 'user' in session:
		
		playersTeamSelection(session['user'],request.form['pn'])

	return redirect(url_for('playerportal')	)
				
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0',debug = True,port=5011)
