
################# Funtions related to server
import os

import pandas as pd
from flask import Flask, send_file

app = Flask(__name__)
current_directory = os.getcwd()

def start_web_server():
    # code to be executed in thread 1
    print("Hello from server!")
    app.run()

@app.route('/')
def hello():
    return send_file(os.path.join(current_directory, 'image/save.png'))

