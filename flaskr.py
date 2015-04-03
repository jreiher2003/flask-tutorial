from flask import Flask, url_for, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
	return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user the porfile for that user
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id , the id is an itergerC
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return "The project page"

@app.route('/about/')
def about():
	return "The about page"

with app.test_request_context('/hello', method='POST'):
	# now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    # assert request.method == 'POST"'

	

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = "Invalid username/password"

	return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)