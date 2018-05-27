from flask import Flask,render_template
from flask_socketio import SocketIO, send, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
list = [];
@app.route('/')
def main():
    return render_template('index.html')
@socketio.on('add')
def adddata():
    x = 0
    json = {'data':x}
    x=x+1
    #print('Message: ' + str(json.data))
    emit('my_add_response',json,broadcast=True)
@socketio.on('subtract')
def subtractdata():
    x = 0
    json = {'data':x}
    x=x-1
    #print('Message: ' + str(json.data))
    emit('my_add_response',json,broadcast=True)
#def han/dleMessage(msg):
#	print('Message: ' + msg)
#	send(msg, broadcast=True)
#send(msg, broadcast=True)

@app.route('/update/')
def update():
    return render_template('update.html')


if __name__ == '__main__':
	socketio.run(app)