from flask import Flask, request, render_template, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
	friends = mysql.query_db("SELECT name, age, DATE_FORMAT(c_date, '%M %D') AS c_date, DATE_FORMAT(c_date, '%Y') AS c_date2 FROM users")
	print friends
	return render_template('index.html',all_friends=friends)

@app.route('/more', methods=['POST'])
def add():
	query="INSERT INTO users(name,age,c_date,u_date) VALUES(:name2,:age2,NOW(),NOW())"

	data= {
			'name2': request.form['name1'],
			'age2': request.form['age1']
		}

	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)

# DATE_FORMAT(c_date, "%M %D") 