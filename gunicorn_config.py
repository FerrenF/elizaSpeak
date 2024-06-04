# gunicorn_config.py
bind = '0.0.0.0:8000'
workers = 1  # Adjust this based on your machine and app requirements
worker_class = 'eventlet'
