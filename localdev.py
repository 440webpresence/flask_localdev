from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import os 
app = Flask(__name__)
app.config.from_pyfile('madeaconfig.py')
socketio = SocketIO(app)

@app.route('/')
def index():
    return(send_from_directory('.', 'bootstraps.html'))

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.emit('response', 'Server received your message: ' + data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
