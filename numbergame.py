from flask import Flask, request, redirect, render_template, session
import random
app = Flask(__name__)
app.secret_key = "whitney"

@app.route('/')
def index():
	if not 'element' in session:
		session['element'] = "hold"
	if not 'cpnum' in session:
		session['cpnum'] = random.randrange(0,101)
	return render_template('gameindex.html')
@app.route('/run', methods=['POST'])
def run():
	session['usernum'] = int(request.form['num'])
	print session['cpnum']
	print session['usernum']
	if session['usernum'] > session['cpnum']:
		session['element'] = "higher"
		print session['element']
	elif session['usernum'] < session['cpnum']:
		session['element'] = "lower"
		print session['element']
	else :
		session['element'] = "equal"
		print session['element']

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('element')
	return redirect('/')


app.run(debug = True)

