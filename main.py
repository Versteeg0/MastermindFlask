from flask import Flask, render_template, request, Response, g, redirect, url_for, abort, render_template, flash, \
    make_response

from database import Database

app = Flask(__name__)
db = Database()
db.create_tables()


@app.route('/', methods=['GET', 'POST'])
def startPage():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('user.html', name=username)
    else:
        return render_template('start.html')
