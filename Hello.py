from flask import Flask, abort, redirect, url_for, request, render_template, make_response, session, escape
app = Flask(__name__)
app.secret_key = 'potato'
# @app.route('/hello/<name>')
# def hello_world(name):
#     return 'Hello World %s!' % name


# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#     return 'Blog Number %d' %postID


# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number %f' %revNo


# @app.route('/flask')
# def hello_flask():
#     return 'Hello Flask!'


# @app.route('/python/')
# def hello_python():
#     return 'Hello Python!'


# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin!'


# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello %s as Guest!' %guest


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))


# @app.route('/success/<name>')
# def success(name):
#     return 'Welcome %s' % name



# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success',name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success',name=user))


# @app.route('/hello/<int:score>')
# def hello_name(score):
#     return render_template('hello.html', marks=score)


# @app.route('/result')
# def result():
#     dict = {'phy':50, 'che':60, 'maths':70}
#     return render_template('result.html', result=dict)


# @app.route('/')
# def index():
#     return render_template("login.html")


# @app.route('/setcookie', methods=['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['nm']

#     resp = make_response(render_template('readcookie.html'))
#     resp.set_cookie('userID', user)

#     return resp

# @app.route('/getcookie')
# def getcookie():
#     name = request.cookies.get('userID')
#     return '<h1>Welcome '+name+'</h1>'


# @app.route('/')
# def student():
#     return render_template("student.html")


# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template('result.html',result=result)


# @app.route('/')
# def index():
#     if 'username' in session:
#         username = session['username']
#         return 'Logged in as ' + username + '<br>' + \
#             "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = 'login'></b>" + \
#         "Click here to log in</b></a>"


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return render_template('session.html')


# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
            return redirect(url_for('success'))
        else:
            flash('You were successfully logged in')
        return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
