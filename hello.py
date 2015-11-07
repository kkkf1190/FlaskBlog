from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
	return "<h1>Hello World</h1>"

@app.route('/user/<username>')
def user(username):
    return '<h1>welcome! %s</h1>' % username

if __name__ == '__main__':
	app.run()
