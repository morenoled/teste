from flask import Flask, request, make_response
from functools import wraps


app = Flask(__name__)


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username1' and auth.password == 'password':
            return f(*args, **kwargs)
        
        return make_response('Could not verufy your login!', 401,{'WWW-Authenticate': 'Basic realm="Login Required"'} )

    return decorated


@app.route('/')
@auth_required
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You are logged in</h1>'

    return make_response ('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required'})


@app.route('/page')
def page():
    return '<h1>You are on the page!</h1>'


@app.route('/otherpage')
@auth_required
def other_page():
    return '<h1>You are on the other page!</h1>'


if __name__ == '__main__':
    app.run(debug=True)