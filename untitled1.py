from flask import Flask

from flask import request

from flask import make_response

from flask import redirect

#from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/response')
def routeResponse():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/request')
def routeRequest():
    user_agent = request.headers.get('User-Agent')
    return 'your userAgent is %s!' % user_agent

@app.route('/redirect')
def routeRedirect():
    return redirect('http://www.baidu.com')


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!<h1>' % name


if __name__ == '__main__':
    app.run()
