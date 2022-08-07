import os
import natsort
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    parent_dir = os.getcwd()
    directory = "static"
    path = os.path.join(parent_dir, directory)
    dir_list = os.listdir(path)
    dir = natsort.natsorted(dir_list)
    return render_template('home.html', len = len(dir_list), dir_list = dir)
 
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)