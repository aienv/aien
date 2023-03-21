from datetime import datetime
#from core.models import UserData , FirmsData
from core import app
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for , send_file
import json
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(APP_ROOT, 'appdata', 'user.json')
FIRM_FILE = os.path.join(APP_ROOT, 'appdata', 'firm.json')
######################################################## 
 # PAGE HANDLERS
########################################################

# URL handler for the "home" page
@app.route('/')
def index():
    return render_template('index.html')

# URL handler for the "erroe calls" page
@app.errorhandler(404)
def not_found(error):
    return render_template('admin/error.html')

# URL handler for the "learn" page
@app.route('/learn')
def learn():
    return render_template('learn.html')

# URL handler for the "business" page
@app.route('/business')
def business():
    return render_template('business.html')

# URL handler for the "products" page
@app.route('/products')
def products():
    return render_template('products.html')

# URL handler for the "join" page
@app.route('/join')
def join():
    return render_template('join.html')

######################################################## 
 # ADMIN HANDLERS
########################################################
STATUS_FILE = os.path.join(APP_ROOT, 'appdata', 'status.json')
@app.route('/admin')
def admin():
    with open(USER_FILE, 'r') as x , open(FIRM_FILE, 'r') as y , open(STATUS_FILE, 'r') as z :
        userdata = json.load(x)
        userdata['users'] = [user for user in reversed(userdata['users'])]
        firmdata = json.load(y)
        firmdata['firms'] = [firm for firm in reversed(firmdata['firms'])]
        state = json.load(z)
    return render_template('admin/index.html' , statedata=state , udata = userdata , fdata = firmdata )

# URL handler for the "admin" page
@app.route('/data')
def data():
    return render_template('admin/data.html')

# URL handler for the "admin" page
@app.route('/404')
def error():
    return render_template('admin/error.html')

######################################################## 
# FORM HANDLERS
########################################################

import core.appdata.status as updater

@app.route('/newuser', methods=['POST'])
def new_user():
    # Read form data
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    location = request.form['location']
    # Read JSON database file
    with open(USER_FILE, 'r') as f:
        data = json.load(f)
    # Get ID for new user
    last_user_id = data['users'][-1]['id']
    new_user_id = last_user_id + 1
    # Create new user dictionary
    new_user = {
        'id': new_user_id,
        'name': fullname,
        'phone': phone,
        'email': email,
        'location': location
    }
    # Append new user to JSON file
    data['users'].append(new_user)
    with open(USER_FILE, 'w') as f:
        json.dump(data, f)
        updater.new_u()
    return render_template('sent.html')


@app.route('/newfirm', methods=['POST'])
def new_firm():
    # Read form data
    phone = request.form['phone']
    email = request.form['email']
    # Read JSON database file
    with open(FIRM_FILE, 'r') as f:
        data = json.load(f)
    # Get ID for new user
    last_firm_id = data['firms'][-1]['id']
    new_firm_id = last_firm_id + 1
    # Create new user dictionary
    new_firm = {
        'id': new_firm_id,
        'phone': phone,
        'email': email,
    }
    # Append new user to JSON file
    data['firms'].append(new_firm)
    with open(FIRM_FILE, 'w') as f:
        json.dump(data, f)
        updater.new_f()
    return render_template('sent.html')

# URL handler for the "delete" page
@app.route('/logs')
def clogs():
    updater.c_log()
    return redirect(url_for('admin'))

# URL handlers to download resources
import core.appdata.excel as xlsx_protocol

@app.route('/download_users', methods=['GET'])
def download_users():
    xlsx_protocol.uhandle()
    # get the music file path from the request
    music_file_path = request.args.get('file_path')

    # send the file to the client
    return send_file(music_file_path, as_attachment=True)

@app.route('/download_firms', methods=['GET'])
def download_firms():
    xlsx_protocol.fhandle()
    # get the music file path from the request
    music_file_path = request.args.get('file_path')

    # send the file to the client
    return send_file(music_file_path, as_attachment=True)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         url = request.form['url']
#         short_id = request.form['custom_id']

#         if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
#             flash('Please enter different custom id!')
#             return redirect(url_for('index'))

#         if not url:
#             flash('The URL is required!')
#             return redirect(url_for('index'))

#         if not short_id:
#             short_id = generate_short_id(8)

#         new_link = ShortUrls(
#             original_url=url, short_id=short_id, created_at=datetime.now())
#         db.session.add(new_link)
#         db.session.commit()
#         short_url = request.host_url + short_id

#         return render_template('index.html', short_url=short_url)

#     return render_template('index.html')

