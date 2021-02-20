from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You are logged in</h1>'

    return make_response ('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required'})

@app.route('/page')
def page():
    return '<h1>You are on the page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)