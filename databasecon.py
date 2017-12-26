import sqlite3
def connection():

	conn = sqlite3.connect('ipl.db',check_same_thread=False)
	c = conn.cursor()
	return conn,c
