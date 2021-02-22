from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "john": "hello",
    "susan": "bye"
}


@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username


@app.route('/')
@auth.login_required
def hello_world():
    return 'Hello, World!'


@app.route('/<username>')
@auth.login_required
def hello_user(username):
    return f'Hello, {username}!'
