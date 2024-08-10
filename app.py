from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello'
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('app.log')  # Log to file
    ]
)

logger = logging.getLogger(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/chat')
def chat():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    if isinstance(data, dict) and 'name' in data and 'message' in data:
        emit('receive_message', data, broadcast=True)
        logger.info("Received message from %s: %s", data['name'], data['message'])
    else:
        logger.warning("Received data is not in the expected format: %s", data)

@socketio.on('send_encrypted_message')
def handle_encrypted_message(data):
    if isinstance(data, dict) and 'name' in data and 'message' in data:
        emit('receive_encrypted_message', data, broadcast=True)
        logger.info("Received encrypted message from %s: %s", data['name'], data['message'])
    else:
        logger.warning("Received data is not in the expected format: %s", data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
