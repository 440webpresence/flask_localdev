from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)
def main():
    a = app.make_config()
    print(a)

def opentxt(thisdir, filename):
    if thisdir == '':
        thisdir = os.getcwd()
        filename = thisdir + '\\' + thisdir 
    
    with open(filename, 'r') as fileio:
        thistxt = fileio.read()
    return(thistxt)

def savetxt(thisdir, filename, txt):
    if thisdir == '':
        thisdir = os.getcwd()
        filename = thisdir + '/' + filename
    with open(filename, 'w') as fileio:
        fileio.write(txt)

if __name__ == "__main__":
    socketio.run(app, debug=True)
    main()