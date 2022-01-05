from flask import Flask, render_template

app=Flask(__name__)

@app.route('/lakshmi')
def lakshmiPage():
	return render_template('lakshmi.html')

@app.route('/ruthvika')
def ruthvikaPage():
	return render_template('ruthvika.html')

if (__name__=="__main__"):
	app.run()
