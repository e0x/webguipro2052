from flask import Flask, request, url_for, redirect, abort, render_template



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('control.html')


@app.route('/runcmd')
@app.route('/runcmd/<button>')
def runcmd(button):
	return 'hello'


if __name__ == '__main__':
	app.debug = True
	app.run()
