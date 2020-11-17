'''Create a chat room application using Flask , socket and HTML. Connect users with socket and authenticate
using username'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfekwiqporyyswsdfg'
socketio = SocketIO(app)

@app.route( '/' )
def hello():
    '''
    :return : return the renderedvalue of HTML
    '''
    return render_template( './ChatApp.html' )

def messageRecived():
    '''
    :return : return the value message Recevied
    '''
    print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
    '''
    :return : return the message
    '''
    print( 'recived my event: ' + str( json ) )
    socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
    socketio.run( app, debug = True )
