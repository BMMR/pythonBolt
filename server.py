
################# Funtions related to server
import os
import pandas as pd
from flask import Flask, send_file
# Import the necessary libraries
import webbrowser

app = Flask(__name__)
current_directory = os.getcwd()


def start_web_server():
    # code to be executed in thread 1
    print("Hello from server!")
    # Open the HTML file in the default web browser
    #webbrowser.open("main_page.html")
    app.run()

# @app.route('/')
# def index():
#     # Read the Excel file
#     df = pd.read_excel("external_info/Battery.xlsx")
#     # Convert the Excel file to HTML
#     html = df.to_html()
#     # Return the HTML to the web page
#     return html

@app.route('/')
def hello():
   return send_file(os.path.join(current_directory, 'image/save.png'))

