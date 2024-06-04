import datetime
import json
import os, sys

from dotenv import load_dotenv
load_dotenv('./.env')

from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet
# Ensure eventlet monkey patching
eventlet.monkey_patch()

p = os.path.abspath(os.getcwd())
newp = os.path.join(p, "eliza_python_translation")
sys.path.insert(0, newp)

from eliza_python_translation.elizalogic import StringTracer, NullTracer, PreTracer
from eliza_python_translation.elizascript import ElizaScriptReader
from eliza_python_translation.eliza import Eliza
from eliza_python_translation.DOCTOR_1966_01_CACM import CACM_1966_01_DOCTOR_script as elizaDoctorScript

RUNNING_FLASK = False

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = os.getenv('COM_SECRET')
app.config['FLASK_DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

socketio = SocketIO(app,  async_mode='eventlet')


def error(message, details):
    return {
        'error_message': message,
        'error_details': json.dumps(details)
    }

def message(id, source, message):
   return  {
        'id': id,
        'timestamp': datetime.datetime.now(),
        'source': source,
        'message': message
    }

def messageTemplateHTML(message):
        return render_template('message.html', **{'message': message})


def throw_tantrum(reasons):
    return render_template('error.html', **reasons)

try:
    status, script = ElizaScriptReader.read_script(elizaDoctorScript)
except RuntimeError as e:
    throw_tantrum(error('Encountered a problem opening script.', e))
    exit(2)

eliza = Eliza(script)
trace = StringTracer()
no_trace = NullTracer()
pre_trace = PreTracer()
eliza.set_tracer(no_trace)


@app.route('/')
def index():

    context = {
        'meta': {
            'APP_NAME': "SpeakEliza"
        },
        'data':
            {
                'messages': list(message(0, 'ELIZA', eliza.get_greeting()))
            }
    }

    return render_template('index.html', **context)


@socketio.on('message')
def handle_message(msg):

    try:
        objp = json.loads(msg)
    except Exception as e:
        return
    if 'message' in objp:
        send(json.dumps({'response': messageTemplateHTML(message(100, 'ELIZA', eliza.response(objp['message'])))}), broadcast=True)


if __name__ == '__main__':

    if RUNNING_FLASK:
        app.run(host='0.0.0.0', port=5000)
    socketio.run(app, debug=False)
