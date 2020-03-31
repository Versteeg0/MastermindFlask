import datetime

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
        user = db.get_user(username)
        if user is None:
            return render_template('usernotfound.html', name=username)
        result = db.get_scores(username)
        scores = []
        for row in result:
            scores.append(
                {'date': datetime.datetime.strptime(row[0], '%Y-%m-%d').strftime('%d-%m-%Y'), 'guesses': row[1]})
        print(scores)
        return render_template('leaderboard.html', name=user[0], scores=scores, times_played=len(scores))


@app.route('/startgame/', methods=['GET', 'POST'])
def game():
    amount_of_boxes = request.form['amount_of_boxes']
    print(amount_of_boxes)
    if request.method == 'POST':
        if amount_of_boxes == '4':
            return render_template('gamefour.html')
        else:
            return render_template('gamesix.html')
