from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/more', methods=['POST'])
def add():
	name=request.form['name1']
	age=request.form['age1']
	# print name///IT WORKS IT CONNECTS
	# print age///IT WORKS IT CONNECTS
	return redirect('/')

app.run(debug=True)