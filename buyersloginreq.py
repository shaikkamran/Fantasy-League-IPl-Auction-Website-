from flask import request
def  abc():
error=''
	try:
		if request.method=="POST":
			attempted_email=request.form['email']
			attempted_pwd=request.form['pwd']
			data=[attempted_email,attempted_pwd]
			m=CheckLoginCredentials(data)
			if m!=0:
				return redirect(url_for('dashboard'))
			else:
