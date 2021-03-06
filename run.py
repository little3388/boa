#!/usr/bin/env python3
"""
run.py

"""
from boa import create_app, socketio
from boa.config import BaseConfig

# initialize Flask app with factory pattern
config = BaseConfig()
app = create_app(config)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
