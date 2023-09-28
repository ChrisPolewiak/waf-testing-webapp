import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/search')
def search():
    args = request.args
    arg_search = args.get("search")

    get_request = {}
    if arg_search != '':
        get_request['search'] = arg_search

    return render_template('index.html', request=get_request)
