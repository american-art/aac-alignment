#!/usr/bin/env python

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import time
import sys
import subprocess
import fcntl
import errno

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

REPOS = set([
    'npg',
    'cbm',
    'wam',
    'nmwa',
])

@app.route('/')
def index():
    return render_template('index.html', repos = REPOS)

@app.route('/<repo_name>')
def repo(repo_name = None):
    if repo_name not in REPOS:
        return 'No such repo'

    config_file = ''
    with open('workflow_config_' + repo_name + '.py', 'r') as f:
        config_file = f.read()

    return render_template(
        'repo.html',
        title = repo_name.upper(),
        repo = repo_name,
        config_file = config_file
    )

@socketio.on('disconnect')
def handle_disconnect():
    pass

@socketio.on('update')
def handle_message(msg):

    emit('start')

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
            shell = True # set true to do it in shell (spark only works in this mode)
        )

        # read and emit
        buf = ''
        while True:
            out = process.stdout.read(1)
            if out == '' and process.poll() is not None:
                break
            if out != '':
                if out == '\n':
                    emit('output', {'data': buf})
                    buf = ''
                else:
                    buf += out
                # sys.stdout.write(out)
                # sys.stdout.flush()

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
    socketio.run(app, host = '127.0.0.1', port = 5000, debug = False)