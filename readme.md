# Eliza Speaks
### A web implementation of the eliza_python_translation library: https://github.com/FerrenF/eliza_python_translation


### Find my libraries at:
* https://github.com/FerrenF/eliza_python_translation

### Find this app at:
* https://github.com/FerrenF/elizaSpeak

#### Find the original library at:
* https://github.com/anthay/ELIZA

#### Currently hosted at:
* https://elizaspeaks.motopc.net/ 
* https://eliza-speaks-0c53907e2dcb.herokuapp.com/

## Pre-requisites

#### Requirements:
-    python-dotenv
-    flask
-    flask-socketio
-    gunicorn
-    eventlet

#### Tested On:
- Heroku, Ubuntu 24.04

## Installation

Installing for the first time:
* Set up your .env file with the template provided.
* Perform "git submodule update --remote"
* In app.py, set the following as applies to you. Heroku does not support some socket functions.
  * RUNNING_FLASK = X,
  * RUNNING_GUNICORN = X
  * DEPLOY_HEROKU = 

Use one of the following:
* flask "app.py:run_flask_app()"
* gunicorn "app:run_app()" -c gunicorn.conf.py

## Issues
Your specific instructions may vary, and you are welcome to post issues - I may reply to them as I find time.