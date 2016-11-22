#!/usr/bin/env python

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
from flask import request, redirect, url_for
from flask_login import current_user, LoginManager, UserMixin, login_required, login_user, logout_user

import time
import sys
import subprocess
import fcntl
import errno
import functools

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, asyc_mode = 'greenlet') #  asyc_mode = 'eventlet'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.session_protection = None
login_manager.init_app(app)

# host should be same in socket front and back end,
# or there will be a cross domain issue
SOCKET = ('127.0.0.1', 5000)

REPOS = set([
    'npg',
    'cbm',
    'wam',
    'nmwa',
])

USERS = {
    'admin': '123', # username (same as session token), password
}

class User(UserMixin):

    def __init__(self, username, password):
        self.id = username
        self.password = password

@login_manager.user_loader
def load_user(session_token):
    username = session_token
    if username in USERS:
        return User(username, USERS[username])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: # already login
        return redirect(request.args.get('next') or url_for('index'))
    # get
    if request.method == 'GET':
        return render_template('login.html')
    # post
    username = request.form['username']
    password = request.form['password']
    if username not in USERS or password != USERS[username]:
        return render_template('login.html')
    login_user(User(username, password))
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', repos = REPOS)

@app.route('/<repo_name>')
@login_required
def repo(repo_name = None):

    print 'repo', current_user
    if repo_name not in REPOS:
        return 'No such repo'

    with open('workflow_config_' + repo_name + '.py', 'r') as f:
        config_file = f.read()

    return render_template(
        'repo.html',
        title = repo_name.upper(),
        repo = repo_name,
        config_file = config_file,
        socket = SOCKET
    )

@socketio.on('connect')
def connect_handler():
    if not current_user.is_authenticated:
        return False  # not allowed here

@socketio.on('disconnect')
def disconnect_handler():
    pass

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        print current_user.is_authenticated
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped

@socketio.on('update')
# @authenticated_only
def handle_message(msg):

    emit('start')
    socketio.sleep(0.1)

    repo = msg['repo']
    if repo not in REPOS:
        emit('end')
        return

    x = open('lock/' + repo, 'w+')

    try:
        # lock
        fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)

        # create subprocess
        process = subprocess.Popen(
            # ["python", "-u", "test.py"], # -u turns off stdout buff for python
            # make sure all python outputs (like logging) all points to stdout
            './remote_auto_update.sh %s' % repo,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            shell = True, # set true to do it in shell (spark only works in this mode)
            bufsize = 1
        )

        for line in iter(process.stdout.readline, b''):
            emit('output', {'data' : line})
            socketio.sleep(0.1)
            print line,
        process.stdout.close()
        process.wait()

    except Exception as e:
        # Resource temporarily unavailable
        if e.errno == errno.EAGAIN:
            emit('output', {'data': 'unavailable'})
        # client disconnect
        elif e.errno == errno.EPIPE:
            pass
        else:
            print e
    finally:
        # unlock
        fcntl.flock(x, fcntl.LOCK_UN)
        x.close()
        emit('end')



if __name__ == '__main__':
    # app.run(host = '127.0.0.1', port = 5000, debug = True)
    socketio.run(app, host = SOCKET[0], port = SOCKET[1], debug = False)