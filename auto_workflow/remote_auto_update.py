#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, disconnect
from flask_login import current_user, LoginManager, UserMixin, login_required, login_user, logout_user
from flask_cors import CORS

import sys
import subprocess
import fcntl
import errno
import functools

# config
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
cors = CORS(app, resources = {r'/*': {'origins': '*'}})
socketio = SocketIO(app, asyc_mode = 'eventlet')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.session_protection = None
login_manager.init_app(app)

USERS = REMOTE_UPDATE_USERS

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
    if repo_name not in REPOS:
        return 'No such repo'

    with open('workflow_config_' + repo_name + '.py', 'r') as f:
        config_file = f.read()

    return render_template(
        'repo.html',
        title = repo_name.upper(),
        repo = repo_name,
        config_file = config_file,
        socket_port = WEB_SOCKET_PORT
    )

@socketio.on('connect')
def connect_handler():
    # current_user will return as anonymous user if the cookie is cross-domain
    if not current_user.is_authenticated:
        return False  # not allowed here

@socketio.on('disconnect')
def disconnect_handler():
    pass

# authentication in socketio
def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped

@socketio.on('update')
@authenticated_only
def update_dev_handler(msg):

    emit('start')
    socketio.sleep(0.1)

    repo = msg['repo']
    if repo not in REPOS:
        emit('output', {'data': 'no such repo'})
        emit('end')
        return

    version = msg['version']
    command = ''
    if version == 'pro':
        command = './remote_auto_update_pro.sh %s' % repo
    else:
        command = './remote_auto_update_dev.sh %s' % repo

    x = open('lock/' + repo, 'w+')
    try:
        # lock
        fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)

        # create subprocess
        process = subprocess.Popen(
            # ["python", "-u", "test.py"], # -u turns off stdout buff for python
            # make sure all python outputs (like logging) all points to stdout
            command,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            shell = True, # set true to do it in shell (spark only works in this mode)
            # bufsize = 1
        )

        for line in iter(process.stdout.readline, b''):
            emit('output', {'data' : line})
            socketio.sleep(0.1)
            # print line,
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
    socketio.run(app, host = '0.0.0.0', port = WEB_SOCKET_PORT, debug = False)