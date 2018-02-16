from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name = request.form['your_name']
	location = request.form['dojo_location']
	language = request.form['favorite_language']
	comment = request.form['comment']

	print name
	print location
	print language
	print comment


	return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)