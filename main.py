from flask import Flask

app = Flask(__name__)


'''
The route() decorator to tell Flask what URL should trigger our function.
The function is given a name which is also used to generate URLs for that particular function, 
and returns the message we want to display in the user’s browser.
'''
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<username>')
def hello_user(username):
    return f'Hello, {username}!'
