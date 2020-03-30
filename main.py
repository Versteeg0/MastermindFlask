from flask import Flask, render_template, request, Response, g, redirect, url_for, abort, render_template, flash, \
    make_response

from database import Database

app = Flask(__name__)
db = Database()
db.create_tables()


@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('user.html', name=username)
    else:
        return render_template('start.html')


@app.route('/leaderboard/<username>', methods=['POST'])
def leaderboard(username):
    if request.method == 'POST':
        db = Database()
        username = request.form['username']
        user = db.get_user(username)
        if user is None:
            return render_template('usernotfound.html', name=username)
        return render_template('leaderboard.html', name=user[0])
